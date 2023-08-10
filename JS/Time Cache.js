// Constructor to initialize the TimeLimitedCache
var TimeLimitedCache = function() {
    // Using Map to store key-value pairs
    this.pairs = new Map();
};

/** 
 * Sets a key-value pair in the cache with a specified expiration duration.
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    // Check if key exists and value is not -1 (expired)
    const vol = this.pairs.get(key);
    const ans = vol && (vol !== -1) ? true : false;

    // Set the value, duration, and index for the given key in the map
    this.pairs.set(key, {
        val: value,
        dur: duration,
        index: (vol?.index ?? 0) + 1,
    });

    // Recursive function to handle expiration
    const lll = (duration, ind) => {
        // Schedule a function to be called after the specified duration
        setTimeout(() => {
            const volIn = this.pairs.get(key);
            
            // If key hasn't been updated, mark it as expired (-1)
            // Otherwise, call the function again with updated duration and index
            if (ind === volIn.index) {
                this.pairs.set(key, {
                    ...volIn,
                    val: -1
                });
                return ans;
            }
            lll(volIn.dur, volIn.index);
        }, duration);
    };

    // Call the recursive expiration function
    lll(duration, this.pairs.get(key).index);
    return ans;
};

/** 
 * Retrieves the value associated with a given key.
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    // Return the value if found and not expired, otherwise return -1
    return this.pairs.get(key)?.val ?? -1;
};

/** 
 * Counts the number of non-expired keys present in the cache.
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let sum = 0;
    // Iterate over the key-value pairs in the map
    for (let [key, value] of this.pairs) {
        // If value is not marked as expired, increment the count
        if (value.val !== -1) sum++;
    }
    return sum;
};

// Example usage:
// var obj = new TimeLimitedCache()
// obj.set(1, 42, 1000); // false
// obj.get(1) // 42
// obj.count() // 1
