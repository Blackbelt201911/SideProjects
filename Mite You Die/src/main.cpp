#include <iostream>
#include <raylib.h>
#include <math.h>








bool CheckCollisionLineRec(Vector2 start, Vector2 end, Rectangle rect) {
    float rectX = rect.x;
    float rectY = rect.y;
    float rectWidth = rect.width;
    float rectHeight = rect.height;
    float minX = fminf(start.x, end.x);
    float minY = fminf(start.y, end.y);
    float maxX = fmaxf(start.x, end.x);
    float maxY = fmaxf(start.y, end.y);

    // Check if the line is outside the rectangle
    if (maxX < rectX || minX > rectX + rectWidth || maxY < rectY || minY > rectY + rectHeight) {
        return false;
    }



    // Check if the line intersects with any of the rectangle's sides
    float m = (end.y - start.y) / (end.x - start.x);


    float y1 = m * (rectX - start.x) + start.y;
    float y2 = m * (rectX + rectWidth - start.x) + start.y;
    float x1 = (rectY - start.y) / m + start.x;
    float x2 = (rectY + rectHeight - start.y) / m + start.x;


    return (y1 >= rectY && y1 <= rectY + rectHeight) || (y2 >= rectY && y2 <= rectY + rectHeight) ||
           (x1 >= rectX && x1 <= rectX + rectWidth) || (x2 >= rectX && x2 <= rectX + rectWidth);
}




void updateEnemyPosition(Vector2 &enemyPos, Vector2 playerPos) {
    float speed = 0.01f;
    if (enemyPos.x < playerPos.x) {
        enemyPos.x += speed;
    } else if (enemyPos.x > playerPos.x) {
        enemyPos.x -= speed;
    }




    if (enemyPos.y < playerPos.y) {
        enemyPos.y += speed;
    } else if (enemyPos.y > playerPos.y) {
        enemyPos.y -= speed;
    }
}




void drawstuff()
{
    const int screenWidth = 1000;
    const int screenHeight = 1000;








    InitWindow(screenWidth, screenHeight, "Mite you die?");








    Texture2D sprite = LoadTexture("pixil-frame-0.png");








    Vector2 spritePosition = { static_cast<float>(screenWidth / 2 - sprite.width / 2),
                               static_cast<float>(screenHeight / 2 - sprite.height / 2) };








    Vector2 AIPOS = { static_cast<float>(screenWidth / 2 - sprite.width / 2),
                      static_cast<float>(screenHeight / 2 - sprite.height / 2) };


















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


        Vector2 objectCenter = { AIPOS.x + sprite.width / 2, AIPOS.y + sprite.height / 2 };




        BeginDrawing();








        ClearBackground(RAYWHITE);








        DrawTextureV(sprite, spritePosition, WHITE);
        DrawTextureV(sprite, AIPOS, WHITE);








        for (int i = 0; i < numRays; i++)
        {
            float angle = DEG2RAD * i * angleIncrement;
            float rayX = objectCenter.x + 250 * cos(angle);
            float rayY = objectCenter.y + 250 * sin(angle);








            DrawLine(objectCenter.x, objectCenter.y, rayX, rayY, RED);








            // Check for collision between the line and the sprite's bounding box
            Rectangle spriteRect = { spritePosition.x, spritePosition.y, static_cast<float>(sprite.width), static_cast<float>(sprite.height) };
            Vector2 lineStart = { objectCenter.x, objectCenter.y };
            Vector2 lineEnd = { rayX, rayY };








            if (CheckCollisionLineRec(lineStart, lineEnd, spriteRect))
            {
                updateEnemyPosition(AIPOS, spritePosition);
                DrawText("Collision Detected!", 10, 10, 20, RED);
            }
        }








        EndDrawing();
    }








    CloseWindow();
}








int main()
{
    drawstuff();
}





















