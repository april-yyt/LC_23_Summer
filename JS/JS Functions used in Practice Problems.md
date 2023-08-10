# JS Functions used in Practice Problems

- **`new Map()`:** Initializes a new Map object, which stores key-value pairs. Allows for efficient insertion, deletion, and retrieval.
- **`.get(key)`:** Retrieves the value associated with a key from the map.
- **`.set(key, value)`:** Inserts or updates a key-value pair in the map.
- **`setTimeout(callback, duration)`:** Schedules a function (`callback`) to be called after a specific duration (in milliseconds). Used here to handle the expiration of keys.
- **`for...of`:** Iterates over the entries in an iterable (in this case, a map), allowing you to access both the key and value in each iteration.
- **Optional Chaining (`?.`) and Nullish Coalescing (`??`) Operators:** These are used to handle potential undefined values. The expression `object?.property` returns `undefined` if `object` is null or undefined. The expression `value ?? defaultValue` returns `defaultValue` if `value` is null or undefined.