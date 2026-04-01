// Day 1: Generics practice

// Generic function to reverse an array
function reverseArray<T>(arr: T[]): T[] {
    const reversed = [...arr];
    let left = 0;
    let right = reversed.length - 1;
    while (left < right) {
        [reversed[left], reversed[right]] = [reversed[right], reversed[left]];
        left++;
        right--;
    }
    return reversed;
}

// Generic stack class
class Stack<T> {
    private items: T[] = [];

    push(item: T): void {
        this.items.push(item);
    }

    pop(): T | undefined {
        return this.items.pop();
    }

    peek(): T | undefined {
        return this.items[this.items.length - 1];
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }
}

// Example usage
const numbers = [1, 2, 3, 4, 5];
console.log(reverseArray(numbers)); // [5, 4, 3, 2, 1]

const stringStack = new Stack<string>();
stringStack.push("hello");
stringStack.push("world");
console.log(stringStack.pop()); // "world"
