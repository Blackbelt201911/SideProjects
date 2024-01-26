#include "raylib.h"
#include "stdio.h"
using namespace std;

void player()
{
    
    const int screenWidth = 800;
    const int screenHeight = 450;
    
    Texture2D sprite = LoadTexture("pixil-frame-0.png");
    
    Vector2 spritePosition = { static_cast<float>(screenWidth / 2 - sprite.width / 2),
                               static_cast<float>(screenHeight / 2 - sprite.height / 2) };

    DrawTextureV(sprite, spritePosition, WHITE);
    
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

    DrawTextureV(sprite, spritePosition, WHITE);
}

