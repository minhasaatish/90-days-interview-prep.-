
// 01. Create a generic function `identity` that takes a value of any type and returns it.
function identify<T>(arg: T): T {
    return arg;
}

console.log(identify<string>("Hello, World!")); // Output: Hello, World!
console.log(identify<number>(42)); // Output: 42