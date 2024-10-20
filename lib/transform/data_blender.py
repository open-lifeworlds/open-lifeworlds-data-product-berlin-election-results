import json
import os
import warnings

import pandas as pd

from lib.tracking_decorator import TrackingDecorator

warnings.filterwarnings("ignore", category=UserWarning)


@TrackingDecorator.track_time
def blend_data(
    data_transformation, source_path, results_path, clean=False, quiet=False
):
    already_exists, converted, exception = 0, 0, 0

    for input_port in data_transformation.input_ports or []:
        for file in input_port.files or []:
            source_file_path = os.path.join(
                source_path, input_port.id, file.source_file_name
            )
            target_file_path = os.path.join(
                results_path, input_port.id, file.target_file_name
            )
            geojson_template_file_path = os.path.join(
                source_path, file.geojson_template_file_name
            )

            try:
                # Load geojson
                with open(
                    file=geojson_template_file_path, mode="r", encoding="utf-8"
                ) as geojson_file:
                    geojson = json.load(geojson_file, strict=False)

                    if not clean and os.path.exists(target_file_path):
                        if not quiet:
                            already_exists += 1
                            print(f"✓ Already exists {file.target_file_name}")
                        continue

                    # Load statistics
                    with open(source_file_path, "r") as csv_file:
                        csv_statistics = pd.read_csv(csv_file, dtype=str)

                        # Iterate over features
                        for feature in geojson["features"]:
                            # Filter statistics
                            statistic_filtered = csv_statistics[
                                csv_statistics["id"]
                                .astype(str)
                                .str.startswith(feature["properties"]["id"])
                            ]

                            # Iterate over attributes
                            for attribute in input_port.attributes:
                                feature["properties"][f"{attribute}"] = (
                                    statistic_filtered[attribute].sum()
                                )

                                if len(statistic_filtered[attribute]) > 1:
                                    feature["properties"][f"{attribute}_avg"] = (
                                        pd.to_numeric(
                                            statistic_filtered[attribute],
                                            errors="coerce",
                                        ).mean()
                                    )

                        os.makedirs(
                            os.path.join(results_path, input_port.id), exist_ok=True
                        )
                        with open(
                            target_file_path, "w", encoding="utf-8"
                        ) as geojson_file:
                            json.dump(geojson, geojson_file, ensure_ascii=False)
                        converted += 1

                        if not quiet:
                            print(f"✓ Convert {os.path.basename(target_file_path)}")

            except Exception as e:
                exception += 1
                print(f"✗️ Exception: {str(e)}")

    print(
        f"blend_data finished with already_exists: {already_exists}, converted: {converted}, exception: {exception}"
    )
