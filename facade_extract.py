from typing import List, Dict, Any

def detect_floors(entities) -> List[float]:
    # TODO: 실제 수평선 클러스터링
    return [0.0, 3.0, 6.0, 9.0]

def detect_vertical_grid(entities) -> List[float]:
    # TODO: 실제 수직선 클러스터링
    return [i * 1.8 for i in range(11)]

def classify_openings(entities, layer_hints: Dict[str, int]) -> Dict[str, Any]:
    # TODO: HATCH/닫힌 폴리라인 분석
    return {"windows": [], "walls": [], "bbox": (0.0, 0.0, 18.0, 9.0)}

def compute_wwr(windows, walls, bbox=None) -> float:
    # TODO: 면적 집계
    return 42.0
