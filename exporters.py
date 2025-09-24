from typing import Dict, Any, List
from io import BytesIO
import json

try:
    import ezdxf
except Exception:
    ezdxf = None

def export_svg(option: Dict[str, Any], base_entities: List[Any]) -> str:
    lines = option.get("lines", [])
    xs = [x for (x, _, _, _, _) in lines] + [x2 for (_, _, x2, _, _) in lines] or [0, 1000]
    ys = [y for (_, y, _, _, _) in lines] + [y2 for (_, _, _, y2, _) in lines] or [0, 1000]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    w = max(1, maxx - minx)
    h = max(1, maxy - miny)
    pad = 20
    view_w, view_h = w + pad * 2, h + pad * 2
    svg_lines = []
    for (x1, y1, x2, y2, layer) in lines:
        svg_lines.append(
            f'<line x1="{x1 - minx + pad}" y1="{view_h - (y1 - miny + pad)}" '
            f'x2="{x2 - minx + pad}" y2="{view_h - (y2 - miny + pad)}" '
            f'stroke="black" stroke-width="1" vector-effect="non-scaling-stroke"/>'
        )
    meta = option.get("meta", {})
    meta_text = " | ".join([f"{k}: {v}" for k, v in meta.items()])
    svg = (
        "<svg xmlns='http://www.w3.org/2000/svg' "
        f"width='{max(600, view_w)}' height='{max(400, view_h)}' "
        f"viewBox='0 0 {view_w} {view_h}' style='background:#fff;border:1px solid #ddd;'>"
        f"<g>{''.join(svg_lines)}</g>"
        "<g>"
        f"<rect x='10' y='{view_h - 30}' width='{view_w - 20}' height='20' fill='white' opacity='0.8' />"
        f"<text x='15' y='{view_h - 15}' font-size='12' fill='#333'>{meta_text}</text>"
        "</g>"
        "</svg>"
    )
    return svg

def export_dxf(option: Dict[str, Any], base_entities: List[Any]) -> bytes:
    if ezdxf is None:
        return ("DXF 내보내기를 위해 ezdxf를 설치하세요: pip install ezdxf").encode("utf-8")
    doc = ezdxf.new("R2013")
    msp = doc.modelspace()
    for (x1, y1, x2, y2, layer) in option.get("lines", []):
        msp.add_line((x1, y1), (x2, y2), dxfattribs={"layer": layer})
    bio = BytesIO()
    doc.write(bio)
    return bio.getvalue()

def export_json(option: Dict[str, Any], brief: dict, orientation: str, target_wwr: float, budget: str) -> str:
    payload = {
        "proposal": option.get("meta", {}),
        "brief": brief,
        "params": {"orientation": orientation, "target_wwr": target_wwr, "budget": budget},
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)
