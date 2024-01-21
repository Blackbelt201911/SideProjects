#include "test.cpp"
#include "raylib.h"


int main(void)
{
   
    const int screenWidth = 800;
    const int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "raylib [core] example - basic window");

    SetTargetFPS(60);              

    // Main game loop
    while (!WindowShouldClose())    
    {

        BeginDrawing();

            ClearBackground(RAYWHITE);

            pain();

        EndDrawing();

    }

    CloseWindow();        

    return 0;
}
