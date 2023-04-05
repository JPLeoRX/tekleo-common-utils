from typing import List
from injectable import injectable


@injectable
class UtilsMath:
    # Remove values in a list that are too close to each other
    # List must be unique and sorted
    def reduce_list_int(self, values: List[int], reduction_delta: int = 1) -> List[int]:
        # If there are less than 2 elements - exit directly
        if len(values) < 2:
            return values

        # Resort the list
        values = sorted(set(values))

        # Go over each pair of values
        for i in range(0, len(values) - 1):
            current_value = values[i]
            next_value = values[i + 1]
            delta = abs(next_value - current_value)

            # If this is a candidate for reduction
            if delta <= reduction_delta:
                # Compute new value (as a midpoint) and replace it in the list
                new_value = int((current_value + next_value) / 2)
                values[i] = new_value
                values[i + 1] = new_value
                values = sorted(set(values))

                # Recursive call
                return self.reduce_list_int(values, reduction_delta)

        return values
