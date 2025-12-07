def is_empty(*values):
    return any(v.strip() == "" for v in values)


def is_valid_marks(*values):
    try:
        for v in values:
            m = int(v)
            if m < 0 or m > 100:
                return False
        return True
    except ValueError:
        return False
