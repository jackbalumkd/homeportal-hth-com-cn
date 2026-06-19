from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    note: str
    source_url: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def to_full_text(self) -> str:
        """返回完整的描述文本"""
        base = f"[{self.keyword}] {self.note}"
        if self.source_url:
            base += f"\n来源: {self.source_url}"
        if self.tags:
            base += f"\n标签: {', '.join(self.tags)}"
        return base

    def to_short_form(self) -> str:
        """返回精简的单行摘要"""
        tag_part = f" ({', '.join(self.tags)})" if self.tags else ""
        return f"{self.keyword}: {self.note[:40]}...{tag_part}"


def format_notes_as_report(notes: List[KeywordNote]) -> str:
    """将多条笔记格式化为可打印的报告"""
    lines = []
    lines.append(f"关键词笔记报告 —— 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 50)
    for i, note in enumerate(notes, 1):
        lines.append(f"{i}. {note.to_full_text()}")
        if i < len(notes):
            lines.append("-" * 30)
    lines.append("=" * 50)
    return "\n".join(lines)


def filter_notes_by_tag(notes: List[KeywordNote], tag: str) -> List[KeywordNote]:
    """按标签筛选笔记"""
    return [n for n in notes if tag.lower() in [t.lower() for t in n.tags]]


def main():
    # 示例数据，包含所给URL和关键词
    sample_notes = [
        KeywordNote(
            keyword="华体会",
            note="用户反馈华体会平台登录体验流畅，界面设计友好。",
            source_url="https://homeportal-hth.com.cn",
            tags=["华体会", "用户体验", "反馈"]
        ),
        KeywordNote(
            keyword="华体会",
            note="华体会系统最近更新了安全验证流程，建议用户关注。",
            source_url="https://homeportal-hth.com.cn",
            tags=["华体会", "安全", "更新"]
        ),
        KeywordNote(
            keyword="华体会",
            note="测试环境报告：华体会模块响应时间符合预期。",
            tags=["华体会", "测试"]
        ),
        KeywordNote(
            keyword="homeportal",
            note="homeportal 主页改版，增加了快捷入口。",
            source_url="https://homeportal-hth.com.cn",
            tags=["homeportal", "前端"]
        ),
    ]

    print("=== 所有笔记完整格式 ===")
    print(format_notes_as_report(sample_notes))

    print("\n=== 按标签筛选结果（标签: 华体会）===")
    filtered = filter_notes_by_tag(sample_notes, "华体会")
    for note in filtered:
        print(note.to_short_form())


if __name__ == "__main__":
    main()