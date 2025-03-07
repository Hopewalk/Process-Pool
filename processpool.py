from multiprocessing import Pool
import time

def task(name):
    print(f"Task {name} is start")
    time.sleep(2)
    print(f"Task {name} is done")
    return f"Task {name} result"

if __name__ == "__main__":
    with Pool(3) as pool:
        results = pool.map(task, range(14))

    print("All tasks are done")
    print("Result:", results)
