# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ClassroomBook
def parse_date(date_str, fmt=None):
    """
    Parse a date string into a datetime.date object.
    
    Supports common formats:
    - YYYY-MM-DD
    - DD/MM/YYYY
    - DD-MM-YYYY
    
    Returns a datetime.date object on success.
    Raises ValueError with a clear message on failure.
    
    Args:
        date_str (str): The date string to parse.
        fmt (str, optional): The expected format string. If None, auto-detect.
    
    Returns:
        datetime.date: The parsed date.
    
    Raises:
        ValueError: If the date string is invalid or unparseable.
    """
    if not isinstance(date_str, str) or not date_str.strip():
        raise ValueError(f"Invalid date string: '{date_str}'")

    # Auto-detect format if not provided
    if fmt is None:
        date_str = date_str.strip()
        if len(date_str) == 10:
            # Try YYYY-MM-DD
            if date_str[4] == '-' and date_str[7] == '-':
                fmt = '%Y-%m-%d'
            elif date_str[2] == '-' and date_str[5] == '-':
                fmt = '%d-%m-%Y'
                date_str = date_str.replace('-', '/')
            elif date_str[2] == '/' and date_str[5] == '/':
                fmt = '%d/%m/%Y'
            else:
                raise ValueError(f"Cannot parse date string: '{date_str}'")
        elif len(date_str) == 10:
            # Try DD/MM/YYYY
            if date_str[2] == '/' and date_str[5] == '/':
                fmt = '%d/%m/%Y'
            elif date_str[2] == '-' and date_str[5] == '-':
                fmt = '%d-%m-%Y'
                date_str = date_str.replace('-', '/')
            else:
                raise ValueError(f"Cannot parse date string: '{date_str}'")
        else:
            raise ValueError(f"Invalid date string length: '{date_str}'")

    try:
        date_obj = datetime.datetime.strptime(date_str, fmt)
        return date_obj.date()
    except ValueError:
        raise ValueError(f"Cannot parse date string '{date_str}' with format '{fmt}'")
