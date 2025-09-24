from pydantic import BaseModel

class BriefState(BaseModel):
    location: str | None = None
    usage: str | None = None
    style: str | None = None
    materials: str | None = None
    site_notes: str | None = None
    constraints: str | None = None

def build_prompt_from_brief(brief: 'BriefState', orientation: str, target_wwr: float, budget: str) -> str:
    return (
        f"[위치] {brief.location or ''}\n"
        f"[용도] {brief.usage or ''}\n"
        f"[스타일] {brief.style or ''}\n"
        f"[재료] {brief.materials or ''}\n"
        f"[부지메모] {brief.site_notes or ''}\n"
        f"[제약] {brief.constraints or ''}\n"
        f"[방위] {orientation} | [목표 WWR] {target_wwr}% | [예산] {budget}\n"
        "[표현] 현대적, 기능적, 에너지효율 중심, 야간 조명 패턴은 모듈 리듬과 일치\n"
    )
