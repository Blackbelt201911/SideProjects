#include <iostream>
#include <raylib.h>
#include "math.h"

void drawstuff()
{
    const int screenWidth = 800;
    const int screenHeight = 450;
    
    InitWindow(screenWidth, screenHeight, "Mite you die?");


    Texture2D sprite = LoadTexture("pixil-frame-0.png");

    Vector2 spritePosition = { static_cast<float>(screenWidth / 2 - sprite.width / 2),
                            static_cast<float>(screenHeight / 2 - sprite.height / 2) };

    Vector2 AIPOS = { static_cast<float>(screenWidth / 2 - sprite.width / 2),
                            static_cast<float>(screenHeight / 2 - sprite.height / 2) };

    Vector2 objectCenter = { AIPOS.x, AIPOS.y }; 


    int numRays = 36; 
    float angleIncrement = 360.0f / numRays;

    SetTargetFPS(60);               

    while (!WindowShouldClose())    
    {
       
        if (IsKeyDown(KEY_D)) {
            spritePosition.x += 2.5f;
        }
        if (IsKeyDown(KEY_A)) {
            spritePosition.x -= 2.5f;
        }
        if (IsKeyDown(KEY_S)) {
            spritePosition.y += 2.5f;
        }
        if (IsKeyDown(KEY_W)) {
            spritePosition.y -= 2.5f;
        }

        BeginDrawing();

            ClearBackground(RAYWHITE);

            DrawTextureV(sprite, spritePosition, WHITE);

            DrawTextureV(sprite, AIPOS, WHITE);


            for (int i = 0; i < numRays; i++)
            {
                float angle = DEG2RAD * i * angleIncrement;
                float rayX = objectCenter.x + 100 * cos(angle);
                float rayY = objectCenter.y + 100 * sin(angle);

                DrawLine(objectCenter.x, objectCenter.y, rayX, rayY, RED);
            }


            

        EndDrawing();
       
    }


    CloseWindow();        

}


int main(){

    drawstuff();
}
