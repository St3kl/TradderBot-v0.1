from app.core.pipeline import TradingPipeline
from app.core.stage_registry import StageRegistry


class PipelineBuilder:

    @staticmethod
    def build():

        pipeline = TradingPipeline()

        for stage in StageRegistry.get_stages():
            pipeline.add_step(stage)

        return pipeline