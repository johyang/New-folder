def fibonacci_sequence(n):
    result = []
    a = 0
    b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def calculate_fibonacci_stats(sequence_length):
    sequence = fibonacci_sequence(sequence_length)
    stats = {
        'sequence': sequence,
        'average': sum(sequence) / len(sequence) if sequence else 0,
        'maximum': max(sequence) if sequence else 0,
        'minimum': min(sequence) if sequence else 0,
        'length': len(sequence)
    }
    return stats