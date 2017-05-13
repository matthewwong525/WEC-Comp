import json
from random import randrange, sample
from collections import OrderedDict

max_time = 1000


def test_case(floors, elevators, num_events):
    events = []
    for i in range(num_events):
        # Most events going up at the start, when it is easy to be > i
        if randrange(num_events) >= i:
            # going up
            start, end = sorted(sample(range(floors), 2))

        else:
            start, end = sorted(sample(range(floors), 2))[::-1]

        assert (0 <= start < floors)
        assert (0 <= end < floors)

        time = randrange(int(i * max_time / num_events), int((i + 1) * max_time / num_events))
        time = min(time, max_time)
        time = max(time, 0)

        events.append(OrderedDict([
            ("time", time),
            ("start", start),
            ("end", end),
        ]))

    output = OrderedDict([
        ("floors", floors),
        ("elevators", elevators),
        ("events", events)
    ])

    return output

output = test_case(10, 1, 400)
print(output)