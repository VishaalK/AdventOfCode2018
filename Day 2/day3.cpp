#include <iostream>
using namespace std;

// The number of inches between the left edge of the fabric and the left edge of the rectangle.
// The number of inches between the top edge of the fabric and the top edge of the rectangle.
// The width of the rectangle in inches.
// The height of the rectangle in inches.
// A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:
struct Claim {
    int left;
    int top;
    int width;
    int height:

    Claim(
        int _left, 
        int _top, 
        int _width, 
        int _height): left(_left), top(_top), width(_width), height(_height): {}
}

int main() {
    // ?
}