import math
from typing import List
from injectable import injectable
from tekleo_common_message_protocol import PointRelative


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

    def points_add(self, point_a: PointRelative, point_b: PointRelative) -> PointRelative:
        return PointRelative(
            point_a.x + point_b.x,
            point_a.y + point_b.y
        )

    def points_subtract(self, point_a: PointRelative, point_b: PointRelative) -> PointRelative:
        return PointRelative(
            point_a.x - point_b.x,
            point_a.y - point_b.y
        )

    def points_multiply(self, point_a: PointRelative, point_b: PointRelative) -> PointRelative:
        return PointRelative(
            point_a.x * point_b.x - point_a.y * point_b.y,
            point_a.x * point_b.y + point_a.y * point_b.x
        )

    def point_multiply(self, point_a: PointRelative, c: float) -> PointRelative:
        return PointRelative(
            point_a.x * c,
            point_a.y * c
        )

    def point_rotate(self, point_a: PointRelative, point_center: PointRelative, angle: float) -> PointRelative:
        angle_radians = math.radians(angle)
        angle_cos = math.cos(angle_radians)
        angle_sin = math.sin(angle_radians)
        point_a_shifted = self.points_subtract(point_a, point_center)
        point_a_rotated = self.points_multiply(point_a_shifted, PointRelative(angle_cos, angle_sin))
        point_a_rotated_back = self.points_add(point_a_rotated, point_center)
        return point_a_rotated_back