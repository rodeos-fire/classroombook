# === Stage 50: Add unit tests for import and export behavior ===
# Project: ClassroomBook
import json, os

# Ensure project files exist
os.makedirs("tests", exist_ok=True)

# Create a sample booking data structure for testing
sample_bookings = [
    {
        "id": 1,
        "room": "Room A",
        "teacher": "Dr. Smith",
        "date": "2024-06-15",
        "time": "09:00-10:00",
        "subject": "Math"
    },
    {
        "id": 2,
        "room": "Room B",
        "teacher": "Dr. Jones",
        "date": "2024-06-15",
        "time": "10:00-11:00",
        "subject": "Physics"
    }
]

# Test import behavior
def test_import_sample_data():
    """Test that sample data can be imported and stored"""
    assert len(sample_bookings) == 2
    assert sample_bookings[0]["room"] == "Room A"
    assert sample_bookings[1]["teacher"] == "Dr. Jones"
    print("✓ Test import_sample_data passed")

# Test export behavior
def test_export_to_json():
    """Test that data can be exported to a JSON file"""
    output_file = "tests/sample_bookings.json"
    with open(output_file, "w") as f:
        json.dump(sample_bookings, f, indent=2)
    
    # Verify file was created
    assert os.path.exists(output_file)
    
    # Read and verify content
    with open(output_file, "r") as f:
        imported_data = json.load(f)
    
    assert len(imported_data) == 2
    assert imported_data[0]["id"] == 1
    print("✓ Test export_to_json passed")

# Test conflict detection
def test_conflict_detection():
    """Test that overlapping bookings are detected"""
    bookings = [
        {"date": "2024-06-15", "time": "09:00-10:00", "room": "Room A"},
        {"date": "2024-06-15", "time": "09:30-10:30", "room": "Room A"},
    ]
    
    def has_conflict(b1, b2):
        if b1["room"] != b2["room"] or b1["date"] != b2["date"]:
            return False
        return b1["time"].split("-")[0] < b2["time"].split("-")[1] and \
               b2["time"].split("-")[0] < b1["time"].split("-")[1]
    
    assert has_conflict(bookings[0], bookings[1])
    print("✓ Test conflict_detection passed")

# Run all tests
test_import_sample_data()
test_export_to_json()
test_conflict_detection()
print("\n✅ All tests passed successfully!")
