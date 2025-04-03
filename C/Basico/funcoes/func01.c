#include <stdio.h>

int main(int argc, char *argv[]){

    for(int i=0; i < argc; i++){
        printf("Arg[%i] %s\n", i, argv[i]);
    }
    return 0;
  }

    float intToFloat (int n){
        return n;
    }

    void halfConvert (int n){
        float half = n * 0.5;
        printf("Metade %.2\n", half);
    }

    int main(){
        halfConvert(5);
        return 0;
    }














    typedef struct 
    {
        char name[MAX_STR];
        float power;
        int lives;
        bool alive;
    } Player;

    void impimePlayer(Player *p){
        printf("=== GAME OVER ===\n");
        printf("%s\n", p->name);
        printf("%,4\n", p->power);
        printf("%d\n", p->lives);
        printf("%i\n", p->alive);
        printf("=================\n");
    }
    int main(){}
    