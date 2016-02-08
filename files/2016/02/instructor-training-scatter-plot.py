import matplotlib.pyplot as plt

live_learners = [43, 31, 41, 20, 44, 46]
live_completion = [65.1, 35.5, 43.9, 35, 43.2, 87]
live_taught = [53.5, 29, 36.6, 35, 34.1, 65.2]

online_learners = [20, 25, 12, 27, 45, 41, 57, 67, 58, 29, 59, 81, 125]
online_completion = [85, 60, 33.3, 59.3, 40, 48.8, 33.3, 23.9, 34.5, 10.3, 39, 46.9, 33.6]
online_taught = [85, 60, 33.3, 59.3, 31.1, 43.9, 28.1, 20.9, 19, 0, 27.1, 34.6, 18.4]

size = 200

plt.figure(1)

p1 = plt.subplot(121)
p1.set_ylim([-10, 100])
plt.scatter(live_learners, live_completion, c='red', label='live', s=size)
plt.scatter(online_learners, online_completion, c='blue', label='online', s=size)
plt.xlabel('Number of participants')
plt.ylabel('Completion %')
plt.legend()
plt.grid(True)

p2 = plt.subplot(122)
p2.set_ylim([-10, 100])
plt.scatter(live_learners, live_taught, c='red', label='live', s=size)
plt.scatter(online_learners, online_taught, c='blue', label='online', s=size)
plt.xlabel('Number of participants')
plt.ylabel('Teaching within first year %')
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig('training.png')
