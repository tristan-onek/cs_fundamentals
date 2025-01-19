#include <iostream>
#include <vector>
#include <cmath>

// Define a Vector class
class Vector {
public:
    std::vector<double> values;

    // Constructor
    Vector(std::initializer_list<double> init) : values(init) {}

    // Magnitude
    double magnitude() const {
        double sum = 0;
        for (double val : values)
            sum += val * val;
        return std::sqrt(sum);
    }

    // Dot product
    double dot(const Vector& other) const {
        double result = 0;
        for (size_t i = 0; i < values.size(); ++i)
            result += values[i] * other.values[i];
        return result;
    }

    // Scalar multiplication
    Vector scale(double scalar) const {
        Vector result = *this;
        for (double& val : result.values)
            val *= scalar;
        return result;
    }

    // Print vector
    void print() const {
        for (double val : values)
            std::cout << val << " ";
        std::cout << std::endl;
    }
};
