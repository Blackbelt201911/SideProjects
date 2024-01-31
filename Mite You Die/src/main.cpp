#include "raylib.h"


int main(void)
{

    const int screenWidth = 1000;
    const int screenHeight = 1000;

    bool titleScreen = true;

    

    InitWindow(screenWidth, screenHeight, "Mite You Die?");

    SetTargetFPS(60);               
    
    while (!WindowShouldClose())   
    {
        
        BeginDrawing();

            ClearBackground(RAYWHITE);


        EndDrawing();

    }

    
    CloseWindow();       

    return 0;
}