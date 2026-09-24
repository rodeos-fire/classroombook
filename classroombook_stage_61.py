# === Stage 61: Add performance timing for core list and search operations ===
# Project: ClassroomBook
import time

def benchmark_list_operations(rooms, teachers, timeslots):
    """Benchmark core list and search operations."""
    times = {}
    start = time.perf_counter_ns()
    total_rooms = len(rooms)
    times["total_rooms"] = time.perf_counter_ns() - start
    
    start = time.perf_counter_ns()
    total_teachers = len(teachers)
    times["total_teachers"] = time.perf_counter_ns() - start
    
    start = time.perf_counter_ns()
    total_timeslots = len(timeslots)
    times["total_timeslots"] = time.perf_counter_ns() - start
    
    start = time.perf_counter_ns()
    room_search = [r for r in rooms if r.id % 2 == 0]
    times["room_search"] = time.perf_counter_ns() - start
    
    start = time.perf_counter_ns()
    teacher_search = [t for t in teachers if t.id % 2 == 0]
    times["teacher_search"] = time.perf_counter_ns() - start
    
    start = time.perf_counter_ns()
    timeslot_search = [ts for ts in timeslots if ts.id % 2 == 0]
    times["timeslot_search"] = time.perf_counter_ns() - start
    
    return times
