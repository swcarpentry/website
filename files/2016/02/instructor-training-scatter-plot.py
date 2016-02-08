import matplotlib.pyplot as plt
from datetime import date

live_learners = [43, 31, 41, 20, 44, 46]
live_completion = [65.1, 35.5, 43.9, 35, 43.2, 87]
live_taught = [53.5, 29, 36.6, 35, 34.1, 65.2]
live_start = [date(2014, 4, 28), date(2014, 9, 22), date(2014, 10, 22), date(2014, 11, 12), date(2015, 1, 6), date(2015, 2, 11)]

online_learners = [20, 25, 12, 27, 45, 41, 57, 67, 58, 29, 59, 81, 125]
online_completion = [85, 60, 33.3, 59.3, 40, 48.8, 33.3, 23.9, 34.5, 10.3, 39, 46.9, 33.6]
online_taught = [85, 60, 33.3, 59.3, 31.1, 43.9, 28.1, 20.9, 19, 0, 27.1, 34.6, 18.4]
online_start = [date(2012, 8, 26), date(2012, 10, 11), date(2013, 1, 6), date(2013, 3, 12), date(2013, 5, 12), date(2013, 8, 12), date(2013, 9, 30), date(2014, 1, 16), date(2014, 4, 24), date(2014, 6, 5), date(2014, 6, 11), date(2014, 9, 10), date(2015, 2, 1)]

plt.figure(1)

p221 = plt.subplot(2, 2, 1)
p221.set_ylim([-10, 100])
plt.scatter(live_learners, live_completion, c='red', label='live', s=30)
plt.scatter(online_learners, online_completion, c='blue', label='online', s=30)
plt.xlabel('Number of participants')
plt.ylabel('Completion %')
plt.grid(True)
plt.legend()

p222 = plt.subplot(2, 2, 2)
p222.set_ylim([-10, 100])
plt.scatter(live_learners, live_taught, c='red', label='live', s=30)
plt.scatter(online_learners, online_taught, c='blue', label='online', s=30)
plt.xlabel('Number of participants')
plt.ylabel('Teaching within first year %')
plt.grid(True)
plt.legend()

p223 = plt.subplot(2, 2, 3)
p223.set_ylim([-10, 100])
plt.plot_date(live_start, live_learners, c='red', label='live')
plt.plot_date(online_start, online_learners, c='blue', label='online')
plt.xlabel('Course date')
plt.ylabel('Number of participants')
plt.grid(True)
plt.legend()
_, labels = plt.xticks()
plt.setp(labels, rotation=90)

p224 = plt.subplot(2, 2, 4)
p224.set_ylim([-10, 100])
plt.plot_date(live_start, live_taught, c='red', label='live')
plt.plot_date(online_start, online_taught, c='blue', label='online')
plt.xlabel('Course date')
plt.ylabel('Teaching within first year %')
plt.grid(True)
plt.legend()
_, labels = plt.xticks()
plt.setp(labels, rotation=90)

plt.tight_layout()
plt.savefig('training.png')
