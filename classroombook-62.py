# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ClassroomBook
def score_timeslot(timeslot, room, teacher, booked_slots, room_capacity=30):
    """Score a candidate (room, timeslot) for a given teacher.

    Higher scores mean better recommendations.

    Parameters
    ----------
    timeslot : dict
        Must have keys 'day', 'hour'.
    room : dict
        Must have keys 'name', 'capacity'.
    teacher : dict
        Must have keys 'name', 'preferred_days', 'preferred_hours',
        'preferred_rooms'.
    booked_slots : list[dict]
        All already-booked timeslots in the system.
    room_capacity : int
        Maximum occupancy for the room.

    Returns
    -------
    float
        Composite score (higher = better).
    """
    score = 0.0

    # Prefer the teacher's favourite days
    if timeslot['day'] in teacher.get('preferred_days', []):
        score += 1.0

    # Prefer the teacher's favourite hours
    if timeslot['hour'] in teacher.get('preferred_hours', []):
        score += 0.5

    # Prefer the teacher's favourite rooms
    if room['name'] in teacher.get('preferred_rooms', []):
        score += 1.5

    # Slight bonus for rooms that are closer to the teacher's preference
    if room['name'] in teacher.get('preferred_rooms', []):
        score += 0.3 * (room['capacity'] - 20)

    # Penalise if the room is already heavily booked on that day
    day_booked = [s for s in booked_slots if s['day'] == timeslot['day'] and s['hour'] == timeslot['hour']]
    if day_booked:
        score -= 0.5 * len(day_booked)

    # Reward rooms with higher capacity (more flexible)
    score += 0.1 * room['capacity']

    return score
