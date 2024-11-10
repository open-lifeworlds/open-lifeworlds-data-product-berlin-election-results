import json
import os
import warnings
from dataclasses import asdict

import yaml

from config.data_product_manifest_loader import File, QualityMetric
from lib.tracking_decorator import TrackingDecorator

warnings.filterwarnings("ignore", category=UserWarning)


class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


@TrackingDecorator.track_time
def generate_geojson_property_completeness_metrics(
    data_product_manifest, config_path, data_transformation, results_path
):
    data_product_manifest_path = os.path.join(config_path, "data-product-manifest.yml")

    files = []

    # Iterate over input ports
    for input_port in data_transformation.input_ports or []:
        for file in input_port.files or []:
            target_file_path = os.path.join(
                results_path, input_port.id, file.target_file_name
            )

            # Load geojson
            with open(
                file=target_file_path, mode="r", encoding="utf-8"
            ) as geojson_file:
                geojson = json.load(geojson_file, strict=False)

                count = 0
                count_all = len(geojson["features"])

                for feature in geojson["features"]:
                    if all(
                        property in feature["properties"]
                        for property in input_port.attributes
                    ):
                        count += 1

                files.append(
                    File(
                        name=file.target_file_name,
                        value=count / len(geojson["features"]),
                    )
                )

                print(
                    f"{str(count).rjust(4)} / {str(count_all).rjust(4)} ({str(round((count / count_all * 100))).rjust(3)}%) {file.target_file_name}"
                )

    if data_product_manifest.observability.quality is None or not any(
        metric
        for metric in data_product_manifest.observability.quality
        if metric.name == "geojson_property_completeness"
    ):
        # Create the observability section if it does not exist
        if data_product_manifest.observability.quality is None:
            data_product_manifest.observability.quality = []

        # Append the quality metric to the data product manifest
        data_product_manifest.observability.quality.append(
            QualityMetric(
                name="geojson_property_completeness",
                description="The percentage of geojson features that have all necessary properties",
                files=files,
            )
        )

    with open(data_product_manifest_path, "w") as file:
        yaml.dump(
            asdict(data_product_manifest),
            file,
            sort_keys=False,
            default_flow_style=False,
            Dumper=IndentDumper,
            allow_unicode=True,
            width=float("inf"),
            explicit_start=True,
        )
