from git import Repo, Actor
from datetime import datetime, timedelta

repo = Repo.init('.')
git = repo.git
git.update_ref("HEAD", d=True)
index = repo.index
actor = Actor("Ciarán Ó hAoláin", "ciaran@cohaolain.ie")

with open('art.csv') as art_file:
    art = list(
        map(lambda x: list(map(lambda y: 1 if y else 0, x.strip().split(","))),
            art_file.readlines()))

for i, weekday in enumerate(art):
    if len(weekday) < 52:
        weekday.extend([0 for _ in range(52 - len(weekday))])
if len(art) < 7:
    art.extend([[0 for _ in range(52)] for _ in range(7 - len(art))])


art = list(map(list, zip(*art)))

flattened_art = [item for sublist in art for item in sublist]

start_date = (datetime.today() - timedelta(days=365)
              ).replace(microsecond=0)

while start_date.weekday() != 6:
    start_date -= timedelta(days=1)


time = start_date
while flattened_art:
    if flattened_art.pop(0):
        for _ in range(100):
            index.commit(str(time), author=actor, committer=actor,
                         commit_date=time.isoformat(),
                         author_date=time.isoformat())
    time += timedelta(days=1)
