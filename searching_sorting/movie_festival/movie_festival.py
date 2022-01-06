from sys import stdin

def max_movies(movie_times):
    movie_times.sort(key=lambda time: time[1])
    max_movies = 0
    current_end = -1
    for i in range(len(movie_times)):
        start, end = movie_times[i]
        if current_end <= start:
            max_movies += 1
            current_end = end
    return max_movies

if __name__ == '__main__':
    _ = stdin.readline()
    movie_times = []
    for line in stdin.readlines():
        start, end = [int(num) for num in line.split()]
        movie_times.append((start, end))
    print(max_movies(movie_times))