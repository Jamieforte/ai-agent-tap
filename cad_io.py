from typing import Tuple, List, Dict, Any
import io

try:
    import ezdxf  # pip install ezdxf
except Exception:
    ezdxf = None

HINTS = ["ELV", "ELEV", "입면", "立面"]

def load_cad(file_like) -> Tuple[List[Any], Dict[str, Any]]:
    name = getattr(file_like, "name", "upload")
    suffix = name.split(".")[-1].lower()

    if suffix == "dwg":
        # TODO: ODA CLI 연동하여 DXF 변환
        return _stub_entities(), {"layers": {}, "note": "DWG는 DXF 변환 필요(ODA CLI 예정)"}

    if suffix != "dxf":
        raise ValueError("지원 포맷: DXF/DWG")

    if ezdxf is None:
        return _stub_entities(), {"layers": {}, "note": "ezdxf 미설치(stub)"}

    data = file_like.read()
    bio = io.BytesIO(data)
    try:
        doc = ezdxf.read(bio)
    except Exception:
        bio.seek(0)
        doc = ezdxf.readfile(bio)

    msp = doc.modelspace()
    ents = [e for e in msp]
    layer_names = set(getattr(e.dxf, "layer", "0") for e in ents if hasattr(e, "dxf"))
    score = {L: sum(1 for h in HINTS if h.lower() in L.lower()) for L in layer_names}
    return ents, {"layers": score, "units": getattr(doc, "units", None)}

def _stub_entities():
    return []
