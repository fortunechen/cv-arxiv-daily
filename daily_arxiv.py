import arxiv
from datetime import datetime, timedelta

def fetch_papers(query, max_results=20):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    return [result for result in search.results()]

# 定义查询条件
cv_query = 'cat:cs.CV'  # 计算机视觉主分类
video_gen_query = 'cat:cs.CV AND (all:"video generation" OR all:"text-to-video")'  # 视频生成关键词

# 获取论文
cv_papers = fetch_papers(cv_query)
video_papers = fetch_papers(video_gen_query)

# 生成Markdown表格
def generate_md_table(papers, title):
    md = f"### {title}\n| Date | Title | Authors | PDF |\n|------|-------|---------|-----|\n"
    for paper in papers:
        md += f"| {paper.published.date()} | {paper.title} | {', '.join(str(a) for a in paper.authors)} | [PDF]({paper.pdf_url}) |\n"
    return md

with open("README.md", "w") as f:
    f.write(f"# arXiv CV Daily Report ({datetime.today().date()})\n")
    f.write(generate_md_table(cv_papers, "Top 20 CV Papers"))
    f.write("\n")
    f.write(generate_md_table(video_papers, "Video Generation Papers"))
