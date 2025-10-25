# Circle Edge Collision Explanation

## Your Circle in the Window

Your circle has:

* **Center coordinates:** `(x, y)`
* **Radius:** `radius`

Your window has:

* **Width:** `Width`
* **Height:** `Height`

The circle’s edge is at:

* **Left edge:** `x - radius`
* **Right edge:** `x + radius`
* **Top edge:** `y - radius`
* **Bottom edge:** `y + radius`

---

## Collision Logic

```python
if x - radius <= 0 or x + radius >= Width or y - radius <= 0 or y + radius >= Height:
    running = False
```

1. **`x - radius <= 0`**
   Checks if the **left edge of the circle** has gone past the **left side of the window** (`x = 0`).
   ✅ Collision with **left wall**.

2. **`x + radius >= Width`**
   Checks if the **right edge of the circle** has gone past the **right side of the window** (`x = Width`).
   ✅ Collision with **right wall**.

3. **`y - radius <= 0`**
   Checks if the **top edge of the circle** has gone past the **top of the window** (`y = 0`).
   ✅ Collision with **top wall**.

4. **`y + radius >= Height`**
   Checks if the **bottom edge of the circle** has gone past the **bottom of the window** (`y = Height`).
   ✅ Collision with **bottom wall**.

If **any** of these conditions are true, the circle has touched or gone past a boundary → **game over**.

---

### Example

* **Window:** `Width = 800`, `Height = 600`
* **Circle:** `radius = 30`, `x = 790`, `y = 300`

Check:

* `x + radius = 790 + 30 = 820` → `820 >= 800` ✅ Collision with **right wall**
  Game ends because the **circle is partially outside** the right edge.
