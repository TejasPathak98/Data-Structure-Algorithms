class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while ty >= sy and tx >= sx:
            if ty == sy:
                return (tx - sx) % ty == 0
            if tx == sx:
                return (ty - sy) % sx == 0
            if ty > tx:
                ty = ty % tx
            else:
                tx = tx % ty
        return False

        