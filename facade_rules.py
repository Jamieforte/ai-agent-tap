from typing import Dict, Any, List

def propose_options(floors: list, grid_x: list, parts: dict, target_wwr: float, orientation: str, budget: str) -> Dict[str, Dict[str, Any]]:
    height = floors[-1] if floors else 9.0
    width = grid_x[-1] if grid_x else 18.0

    def grid_lines(div_x: int, add_mid_transom: bool) -> List[tuple]:
        lines = []
        for i in range(div_x + 1):
            x = width * i / div_x
            lines.append((x, 0.0, x, height, "PRP-MULLION"))
        for y in floors:
            lines.append((0.0, y, width, y, "PRP-TRANSOM"))
        if add_mid_transom and floors:
            for j in range(len(floors) - 1):
                mid = (floors[j] + floors[j + 1]) / 2.0
                lines.append((0.0, mid, width, mid, "PRP-TRANSOM-MID"))
        return lines

    optA = {"name": "안 A | 커튼월", "lines": grid_lines(12, True),
            "meta": {"strategy": "커튼월", "target_wwr": target_wwr, "predicted_wwr": max(target_wwr, 50), "orientation": orientation, "budget": budget}}
    optB = {"name": "안 B | 펀치드", "lines": grid_lines(8, False),
            "meta": {"strategy": "펀치드", "target_wwr": target_wwr, "predicted_wwr": min(target_wwr, 45), "orientation": orientation, "budget": budget}}
    optC = {"name": "안 C | 더블스킨", "lines": grid_lines(10, True),
            "meta": {"strategy": "더블스킨", "target_wwr": target_wwr, "predicted_wwr": target_wwr + 5, "orientation": orientation, "budget": budget}}
    return {optA["name"]: optA, optB["name"]: optB, optC["name"]: optC}
