#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void string_parse(int time[], char* input){
    int n = 0;
    /*
    if (3 * sizeof(int) != sizeof(time)){
        fprintf(stderr, "The array is the wrong size\n");
        return;
    }
    */
    
    //Clear time array if there is anything in it 
    /*
    for(int i = 0; i < 3; i++){
        time[i] = 0;
    }
    */
    char* token = strtok(input, " ");
    while ( (token) && (n < 3) ){
        
        if( strstr(token, "h") ){
            time[0] = atoi(token);
        } 
        else if ( strstr(token, "m") ){
            time[1] = atoi(token);
        }
        else if ( strstr(token, "s") ) {
            time[2] = atoi(token);
        }

        token = strtok(NULL, " ");
        n++;
    }
    /*
    char* delim = "hms";
    for(int n = 0; n < 3; n++){
        
        
        if (strstr(input, (delim + n)) != NULL) {
            time[n] = atoi(token);
        }
    }
    */
    /*
    time[0] = atoi(token);
    token = strtok(NULL, "m");
    time[1] = atoi(token);
    token = strtok(NULL, "s");
    time[2] = atoi(token);
    */

    return;

    /*
    time[1] = atoi(token);

    char* strarg[6] = {"0", "0", "0", "0", "0", "0"};
    int count = 0;

    while( (token != NULL) && (count < 6) ){
        strarg[count] = token;
        count++;
        token = strtok(NULL, " ");
    }

    int val = 0;
    int k = 0;
    for(int i = 1; i < 6; i+=2){
        val = atoi(strarg[i - 1]);
        
        if( strcmp(strarg[i],"h") == 0 ){
            time[0] = val;
        }
        else if( strcmp(strarg[i], "m") == 0 ){
            time[1] = val;
        }
        else if( strcmp(strarg[i], "s") == 0 ){
            time[2] = val;
        } 

    }
    
    return;
    */
    /*
    int val, out[3];

    for(int n = 1; n < argc; n+=2){
        if ( val = atoi(argv[n-1]) ) {
            
            if( strcmp(argv[n],"h") == 0 ){
                out[0] = val;
            }
            else if( strcmp(argv[n], "m") == 0 ){
                out[1] = val;
            }
            else if( strcmp(argv[n], "s") == 0 ){
                out[2] = val;
            } 
            else{
                fprintf(stderr, "Missing or unknown arguments");
            }

        }
        else {
            exit(-1);
        }
    }
    */
}
/*
// Test Code 
int main(int argc, char* argv[]){
    int out[3] = {0,0,0}; 
    if (argc == 1){
        printf("No arguments\n");
        return -1;
    }
    string_parse(out, argv[1]);
    
    for(int m = 0; m < 3; m++){
        printf("%i\n", out[m]);
    }
    
    return 0;
}
*/
 