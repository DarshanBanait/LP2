public class MathOperations {

    // Method to add two integers and return the result
    public static Integer add(Integer num1, Integer num2) {
        return num1 + num2;
    }

    // Method to subtract one integer from another and return the result
    public static Integer subtract(Integer num1, Integer num2) {
        return num1 - num2;
    }

    // Method to multiply two integers and return the result
    public static Integer multiply(Integer num1, Integer num2) {
        return num1 * num2;
    }

    // Method to divide one integer by another and return the result
    public static Decimal divide(Integer num1, Integer num2) {
        if (num2 == 0) {
            return null; // Handle division by zero gracefully
        }
        return (Decimal) num1 / num2;
    }
}

// Execute Anonymous Window code

// Test the MathOperations class
Integer num1 = 10;
Integer num2 = 5;

// Perform addition using the MathOperations class
Integer sum = MathOperations.add(num1, num2);
System.debug('Sum: ' + sum);

// Perform subtraction using the MathOperations class
Integer difference = MathOperations.subtract(num1, num2);
System.debug('Difference: ' + difference);

// Perform multiplication using the MathOperations class
Integer product = MathOperations.multiply(num1, num2);
System.debug('Product: ' + product);

// Perform division using the MathOperations class
Decimal quotient = MathOperations.divide(num1, num2);
System.debug('Quotient: ' + quotient);


