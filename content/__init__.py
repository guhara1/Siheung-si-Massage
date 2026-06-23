# 전체 페이지 목록 집계
from . import main, areas, stations, living, themes, info, magazine, about

PAGES = (
    [main.PAGE]
    + areas.PAGES
    + stations.PAGES
    + living.PAGES
    + themes.PAGES
    + info.PAGES
    + magazine.PAGES
    + [about.PAGE]
)
