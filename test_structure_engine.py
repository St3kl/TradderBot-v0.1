from app.market.structure.structure_engine import StructureEngine

highs = [1,2,4,8,5,3,2,5,9,6,3]
lows  = [0,1,2,4,3,1,0,2,4,2,1]
closes = [1,2,3,4,5,6,7,8,9,10,11]

engine = StructureEngine()

structure = engine.analyze(
    highs,
    lows,
    closes
)

print(structure)