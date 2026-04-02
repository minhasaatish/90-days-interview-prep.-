// 01. Stack Class
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

const numberStack = new Stack<number>();
numberStack.push(1);
numberStack.push(2);
console.log(numberStack.peek()); // Output: 2
console.log(numberStack.pop());  // Output: 2
console.log(numberStack.isEmpty()); // Output: false

const stringStack = new Stack<string>();
stringStack.push("Hello");
stringStack.push("World");
console.log(stringStack.peek()); // Output: World
console.log(stringStack.pop());  // Output: World
console.log(stringStack.isEmpty()); // Output: false


// 02. Generic Fetch Function
async function fetchData<T>(url: string): Promise<T> {
    const response = await fetch(url);
    const data: T = await response.json();
    return data;
}

// Example usage of fetchData
interface User {
    id: number;
    name: string;
    email: string;
}

fetchData<User>('https://jsonplaceholder.typicode.com/users/1')
    .then(user => {
        console.log(user.name); // Output: Leanne Graham
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    }); 



// 03. filterByKey 
function filterByKey<T, K extends keyof T>(array: T[], key: K, value: T[K]): T[] {
    return array.filter(item => item[key] === value);
}

// Example usage of filterByKey
interface Product {
    id: number;
    name: string;
    category: string;
}

const products: Product[] = [
    { id: 1, name: 'Laptop', category: 'Electronics' },
    { id: 2, name: 'Shirt', category: 'Clothing' },
    { id: 3, name: 'Phone', category: 'Electronics' },
];

const electronics = filterByKey(products, 'category', 'Electronics');
console.log(electronics); 
// Output: 
// [
//     { id: 1, name: 'Laptop', category: 'Electronics' },
//     { id: 3, name: 'Phone', category: 'Electronics' }
// ]



