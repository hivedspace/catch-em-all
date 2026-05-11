from pathlib import Path

from dagster import AssetSelection, Definitions, DefaultScheduleStatus, ScheduleDefinition, define_asset_job, definitions, load_from_defs_folder
from dagster_duckdb import DuckDBResource

pokeingest_job = define_asset_job(
    name="pokeingest_job",
    selection=AssetSelection.key_prefixes(["pokemon"]),
)

pokeingest_schedule = ScheduleDefinition(
    job=pokeingest_job,
    cron_schedule="0 */3 * * *",
    default_status=DefaultScheduleStatus.RUNNING
)


@definitions
def defs():
    return Definitions.merge(
        load_from_defs_folder(path_within_project=Path(__file__).parent),
        Definitions(
            resources={
                "duckdb": DuckDBResource(
                    database=str(Path(__file__).parent / "defs" / "data" / "hived.duckdb")
                )
            },
            jobs=[pokeingest_job],
            schedules=[pokeingest_schedule],
        ),
    )