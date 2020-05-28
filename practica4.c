#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <conio.h>

#define estados  26
#define simbolos 2

void gotoxy (int x, int y) 
{
	HANDLE hCon = GetStdHandle(STD_OUTPUT_HANDLE);
	COORD dwPos;
	dwPos.X= x;
	dwPos.Y= y;
	SetConsoleCursorPosition(hCon, dwPos);
}

int n_simbolos; 
int n_afd_estados; 
char *edos_aceptacion;   
char aceptados,resp;
int afdtab[estados][simbolos];
char nombre_estados[estados][estados+1];   
int n_optafd_estados;    
int Optafd[estados][simbolos];
char nuevo_final[estados+1];
//Este método dibuja el cuadro inicial en donde se pide el número de estados
void figurita(){
	gotoxy(25,2);printf("+----------------------------------------------+");
	gotoxy(25,4);printf("|----------------------------------------------|");
	int aux;
	for(aux=3;aux<=6;aux++){
		gotoxy(25,aux);printf("|");
		gotoxy(72,aux);printf("|");
	}
	gotoxy(25,7);printf("+----------------------------------------------+");
}
void imprimir_tabla_afd(int tab[][simbolos], int nestados, int nsimbolos,  char *final)
{
    int i, j;

    printf("\nTabla de transicion de estados \n");
    printf("     | ");
    for (i = 0; i < nsimbolos; i++) printf("  %c  ", '0'+i);
    printf("\n-----+--");
    for (i = 0; i < nsimbolos; i++) printf("-----");
    printf("\n");
    for (i = 0; i < nestados; i++) {
        printf("  %c  | ", 'A'+i); 
        for (j = 0; j < nsimbolos; j++)
            printf("  %c  ", tab[i][j]);
        printf("\n");
    }
    printf("Estados de aceptacion = %s\n", final);
}
/*Este método imprime la tabla de transición de forma parcial para que el usuario la complete
de acuerdo a las entradas que desee introducir*/
void cargar_tabla()
{
	figurita();
	gotoxy(28,5);printf("Numero de estados del AFD: ");
	scanf ("%d", &n_afd_estados);
	n_simbolos=2;
	gotoxy(28,9);printf("Ingresa la tabla de transicion: \n");
    gotoxy(28,11);printf("     | ");
    int x,i,j;
    for (i = 0; i < n_simbolos; i++) printf("  %c  ", '0'+i);
    gotoxy(28,12);printf("-----+--");
    for (i = 0; i < n_simbolos; i++) printf("-----");
    printf("\n");
    for (i = 0; i < n_afd_estados; i++) {
        gotoxy(28,13+i);printf("  %c  | ", 'A'+i); 
    }
    /*En este ciclo for es donde el usuario empieza a rellenar la tabla con las transiciones
    entre estados una vez que la tabla de transiciones ya ha sido parcialmente dibujada por el 
    bloque de código anterior*/
    for(x=0;x<n_afd_estados;x++)
	{
		fflush( stdin );
		gotoxy(37,13+x);scanf("%c",&afdtab[x][0]);
		fflush( stdin );
		gotoxy(42,13+x);scanf("%c",&afdtab[x][1]);	
	}
    printf("\n\t\t\t  Ingresa los estados de aceptacion: ");
	fflush(stdin);
    /*Aquí se obtienen los estados de aceptación*/
	scanf("%s",&aceptados);
	edos_aceptacion =&aceptados;	

}
/*
Este método obtiene la cadena del estado siguiente para la cadena del estado actual.
*/
void obtener_estado_sig(char *sig_estados, char *estado_actual,int afd[estados][simbolos], int simbolo)
{
    int i, ch;
    for (i = 0; i < strlen(estado_actual); i++)
        *sig_estados++ = afd[estado_actual[i]-'A'][simbolo];
    *sig_estados = '\0';
}

/*
    Este método obtiene el indice de los estados de equivalencia para el estado 'ch'.
    Los identificadores de clase son '0', '1', '2'
*/
char indice_de_clase_equiv(char ch, char edo[][estados+1], int n)
{
    int i;
    for (i = 0; i < n; i++)
        if (strchr(edo[i], ch)) return i+'0';
    return -1;  /* siguiente estado no definido */
}

/*
    En este método se comprueba si todos los siguientes estados pertenecen a la misma clase de equivalencia.
    Valor de retorno:
        Si el siguiente estado no es unico, devuelve 0.
        Si el siguiente estado es unico, regrese el siguiente estado -> 'A / B / C / ...'
    's' es una cadena '0/1': id de estado
*/
char es_estado_sig(char *s)
{
    char equiv_class;   /* primer clase equivalente */
    while (*s == '@') s++;
    equiv_class = *s++; /* indice de la clase equivalente */
    while (*s) {
        if (*s != '@' && *s != equiv_class) return 0;
        s++;
    }
    return equiv_class; /* siguiente estado, este es de tipo char */
}
int indice_estado(char *state, char edo[][estados+1], int n, int *pn,int cur)  
{
    int i;
    char inf_es_sig[estados+1]; /* informacion del estado siguiente */
    if (!*state) return -1; /* no hay estado siguiente */
    for (i = 0; i < strlen(state); i++)
        inf_es_sig[i] = indice_de_clase_equiv(state[i], edo, n);
    inf_es_sig[i] = '\0';
    printf("   %d:[%s]\t--> [%s] (%s)\n",
        cur, edo[cur], state, inf_es_sig);
    if (i=es_estado_sig(inf_es_sig))
        return i-'0';   /* proximos estados deterministas */
    else {
        strcpy(edo[*pn], inf_es_sig); /* informacion de la division de estados  */
        return (*pn)++;
    }
}
/* Este método divide los estados del afd en final y no final.*/
int clase_init_equiv(char nombre_edo[][estados+1], int n, char *final)
{
    int i, j;
    if (strlen(final) == n) {  /* todos son estados finales */
        strcpy(nombre_edo[0], final);
        return 1;
    }
    strcpy(nombre_edo[1], final);   /* grupo de estados finales  */
    for (i=j=0; i < n; i++) {
        if (i == *final-'A') {
            final++;
        } else nombre_edo[0][j++] = i+'A';
    }
    nombre_edo[0][j] = '\0';
    return 2;
}
/* Obteniendo el afd optimizado */
int obtener_afd_optimizado(char edo[][estados+1], int n,
    int afd[][simbolos], int n_sym, int nuevo_afd[][simbolos])
{
    int n2=n;  
    int i, j;
    char sig_estado[estados+1];
    for (i = 0; i < n; i++) {
        for (j = 0; j < n_sym; j++) { 
            obtener_estado_sig(sig_estado, edo[i], afd, j);
            nuevo_afd[i][j] = indice_estado(sig_estado, edo, n, &n2, i)+'A';
        }
    }
    return n2;
}
/*
    char 'ch' se agrega al final de 's'. Se agrega el caracter nulo \0 para que C lo reconozca como una cadena
*/
void agregar_ch(char *s, char ch)
{
    int n=strlen(s);
    *(s+n) = ch;
    *(s+n+1) = '\0';
}
void ordenar(char edo[][estados+1], int n)
{
    int i, j;
    char temp[estados+1];
    for (i = 0; i < n-1; i++)
        for (j = i+1; j < n; j++)
            if (edo[i][0] > edo[j][0]) {
                strcpy(temp, edo[i]);
                strcpy(edo[i], edo[j]);
                strcpy(edo[j], temp);
            }
}
/*
    Divide la primera clase equivalente en subclases.
    Algoritmo:
        - edo [i1] se divide en 2 o mas clases 's1 / s2 / ...'
        - antiguo equiv. las clases NO se cambian, excepto edo [i1]
        - edo [i1] = s1, edo [n] = s2, edo [n + 1] = s3, ...
    Valor de retorno: numero de NUEVO equiv. clases en 'edo'.
*/
int division_clase_equiv(char edo[][estados+1],
    int i1, /* indice de  'i1'-th clase equiv */
    int i2, /* indice del vector equivalente para 'i1'-th class */
    int n,  /* numero de entradas en 'edo' */
    int n_afd)  /* numero de entradas afd de origen */
{
    char *anterior=edo[i1], *vec=edo[i2];
    int i, n2, flag=0;
    char sig_estado[estados][estados+1];   /* max. 'n' sub clases */
    for (i=0; i < estados; i++) sig_estado[i][0] = '\0';
    for (i=0; vec[i]; i++)
        agregar_ch(sig_estado[vec[i]-'0'], anterior[i]);
    for (i=0, n2=n; i < n_afd; i++) {
        if (sig_estado[i][0]) {
            if (!flag) { 
                strcpy(edo[i1], sig_estado[i]);
                flag = 1;   /* sobrescribir clase principal */
            } else  /* nuevo estado se agrega en 'edo' */
                strcpy(edo[n2++], sig_estado[i]);
        }
    }
    ordenar(edo, n2); /* ordenar clases equivalentes */
    return n2;  /* numero de nuevos estados(clases equivalentes) */
}
/*
clases equivalentes estan segmentadas y obtienen una nueva clase equivalente
*/
int establecer_nueva_clase_equiv(char edo[][estados+1], int n,int nuevo_afd[][simbolos], int n_sym, int n_afd)
{
    int i, j, k;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n_sym; j++) {
            k = nuevo_afd[i][j]-'A';   /* indice del vector equivalente */
            if (k >= n)  /* clase equivalente 'i' debe ser segmentado */
                return division_clase_equiv(edo, i, k, n, n_afd);
        }
    }
    return n;
}
void imprimir_clases(char edo[][estados+1], int n)
{
    int i;
    printf("\nClases equivalentes ==>");
    for (i = 0; i < n; i++)
        printf(" %d:[%s]", i, edo[i]);
    printf("\n");
}
/*
    minimizacion de estados del afd: 'afd' --> 'nuevo_afd'
    Valor de retorno: numero de estados del afd.
*/
int afd_optimizado(
    int afd[][simbolos], /* tabla de transicion del afd */
    int n_afd,  /* numero de estados del afd */
    int n_sym, 
    char *final,   /* estados de aceptacion del afd */
    char edo[][estados+1],  /* nombre de la tabla de estados */
    int nuevo_afd[][simbolos])  /* tabla del afd reducida */
{
    char nextstate[estados+1];
    int n;  /* cantidad de nuevos estados del afd*/
    int n2; 
    n = clase_init_equiv(edo, n_afd, final);
    while (1) {
        imprimir_clases(edo, n);
        n2 = obtener_afd_optimizado(edo, n, afd, n_sym, nuevo_afd);
        if (n != n2)
            n = establecer_nueva_clase_equiv(edo, n, nuevo_afd, n_sym, n_afd);
        else break; /* segmentacion de la clase equivalente concluida!!! */
    }
    return n;   /* numero de estados del afd*/
}
/*
    Comprobar si 't' es un subconjunto de 's'.
*/
int es_sub(char *s, char *t)
{
    int i;
    for (i = 0; *t; i++)
        if (!strchr(s, *t++)) return 0;
    return 1;
}
/*
nuevos estados finales del afd reducido
*/
void nuevos_aceptados(
    char *nuevos,    /* nuevos estados del afd */
    char *anteriores,    /* estados originales  */
    char edo[][estados+1],  /* tabla de estados  */
    int n)  /* numero de estados en 'edo' */
{
    int i;
    for (i = 0; i < n; i++)
        if (es_sub(anteriores, edo[i])) *nuevos++ = i+'A';
    *nuevos++ = '\0';
}

int main()
{
	do{
		system("CLS");
    	system("COLOR F0");
    	printf("//Juarez Espinoza Ulises\n//Garcia Medina Saul");
    	gotoxy(27,3);printf("Minimizacion de un AFD por conjunto cociente");
		cargar_tabla();
    	n_optafd_estados = afd_optimizado(afdtab, n_afd_estados,n_simbolos, edos_aceptacion, nombre_estados, Optafd);
    	nuevos_aceptados(nuevo_final, edos_aceptacion, nombre_estados, n_optafd_estados);
    	imprimir_tabla_afd(Optafd, n_optafd_estados, n_simbolos, nuevo_final);
		printf("\nDesea repetir el programa s/n: ");
        resp=getch();
	}while(resp=='S' || resp=='s'); 
    printf("\n");		
	return 0;

}