#include <iostream>
#include <vector>

// Class Matrix:
class Matrix 
{
  public:
    std::vector<std::vector<double>> values;

    Matrix(std::initializer_list<std::vector<double>> init) : values(init) {} // constructor

    // Transposition:
    Matrix transpose() const 
    {
        size_t rows = values.size();
        size_t cols = values[0].size();
        Matrix result(std::vector<std::vector<double>>(cols, std::vector<double>(rows)));
        for (size_t i = 0; i < rows; ++i)
            for (size_t j = 0; j < cols; ++j)
                result.values[j][i] = values[i][j];
        return result;
    }

    void print() const 
    {
        for (const auto& row : values) 
        {
            for (double val : row)
                std::cout << val << " ";
            std::cout << std::endl;
        }
    }
};
