#include <stdio.h>
#include <string.h>

#define estados  99
#define simbolos 20

int n_simbolos; 
int n_afd_estados; 
char *afd_final;   
char aceptados;
int afdtab[estados][simbolos];

char nombre_estados[estados][estados+1];   

int n_optafd_estados;    
int Optafd[estados][simbolos];
char nuevo_final[estados+1];


void imprimir_tabla_afd(int tab[][simbolos], int nestados, int nsimbolos,  char *final)
{
    int i, j;

    puts("\nafd: Tabla de transicion de estados ");
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

void cargar_tabla()
{
	printf("Numero de estados del AFD: ");
	scanf ("%d", &n_afd_estados);
	n_simbolos=2;
/*	printf("Ingresa los estados finales: ");
	fflush(stdin);
	scanf("%s",&aceptados);*/
	afd_final ="ABCD";	
	printf("\nIngresa la tabla de transicion: \n");
	int x;
	for(x=0;x<n_afd_estados;x++)
	{
		printf("Para 0  afdtab[%d][0]: ",x);
		fflush( stdin );
		scanf("%c",&afdtab[x][0]);
		printf("Para 1  afdtab[%d][1]: ",x);
		fflush( stdin );
		scanf("%c",&afdtab[x][1]);	
	}
	/*
    afdtab[0][0] = 'B'; afdtab[0][1] = 'C';
    afdtab[1][0] = 'B'; afdtab[1][1] = 'D';
    afdtab[2][0] = 'B'; afdtab[2][1] = 'E';
    afdtab[3][0] = 'B'; afdtab[3][1] = 'E';
    afdtab[4][0] = 'E'; afdtab[4][1] = 'E';
	n_afd_estados=5;
	n_simbolos=2;
	afd_final="ABCD";*/

}
/*
Obtener cadena de estado siguiente para cadena de estado actua.
*/
void obtener_estado_sig(char *nextestados, char *estado_actual,int afd[estados][simbolos], int simbolo)
{
    int i, ch;
    for (i = 0; i < strlen(estado_actual); i++)
        *nextestados++ = afd[estado_actual[i]-'A'][simbolo];
    *nextestados = '\0';
}

/*
    Obtener el indice de los estados de equivalencia para el estado 'ch'.
    Los identificadores de clase son '0', '1', '2'
*/
char indice_de_clase_equiv(char ch, char stnt[][estados+1], int n)
{
    int i;
    for (i = 0; i < n; i++)
        if (strchr(stnt[i], ch)) return i+'0';
    return -1;  /* siguiente estado no definido */
}

/*
    Comprobar si todos los siguientes estados pertenecen a la misma clase de equivalencia.
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
int indice_estado(char *state, char stnt[][estados+1], int n, int *pn,int cur)  
{
    int i;
    char state_flags[estados+1]; /* informacion del estado siguiente */
    if (!*state) return -1; /* no hay estado siguiente */
    for (i = 0; i < strlen(state); i++)
        state_flags[i] = indice_de_clase_equiv(state[i], stnt, n);
    state_flags[i] = '\0';
    printf("   %d:[%s]\t--> [%s] (%s)\n",
        cur, stnt[cur], state, state_flags);
    if (i=es_estado_sig(state_flags))
        return i-'0';   /* proximos estados deterministas */
    else {
        strcpy(stnt[*pn], state_flags); /* informacion de la division de estados  */
        return (*pn)++;
    }
}
/* Dividir los estados del afd en final y no final.*/
int clase_init_equiv(char statename[][estados+1], int n, char *final)
{
    int i, j;
    if (strlen(final) == n) {  /* todos son estados finales */
        strcpy(statename[0], final);
        return 1;
    }
    strcpy(statename[1], final);   /* grupo de estados finales  */
    for (i=j=0; i < n; i++) {
        if (i == *final-'A') {
            final++;
        } else statename[0][j++] = i+'A';
    }
    statename[0][j] = '\0';
    return 2;
}
/* Obteniendo el afd optimizado */
int obtener_afd_optimizado(char stnt[][estados+1], int n,
    int afd[][simbolos], int n_sym, int newafd[][simbolos])
{
    int n2=n;  
    int i, j;
    char sig_estado[estados+1];
    for (i = 0; i < n; i++) {
        for (j = 0; j < n_sym; j++) { 
            obtener_estado_sig(sig_estado, stnt[i], afd, j);
            newafd[i][j] = indice_estado(sig_estado, stnt, n, &n2, i)+'A';
        }
    }
    return n2;
}
/*
    char 'ch' se agrega al final de 's'.
*/
void agregar_ch(char *s, char ch)
{
    int n=strlen(s);
    *(s+n) = ch;
    *(s+n+1) = '\0';
}
void ordenar(char stnt[][estados+1], int n)
{
    int i, j;
    char temp[estados+1];
    for (i = 0; i < n-1; i++)
        for (j = i+1; j < n; j++)
            if (stnt[i][0] > stnt[j][0]) {
                strcpy(temp, stnt[i]);
                strcpy(stnt[i], stnt[j]);
                strcpy(stnt[j], temp);
            }
}
/*
    Divide la primera clase equivalente en subclases.
    Algoritmo:
        - stnt [i1] se divide en 2 o mÃ¡s clases 's1 / s2 / ...'
        - antiguo equiv. las clases NO se cambian, excepto stnt [i1]
        - stnt [i1] = s1, stnt [n] = s2, stnt [n + 1] = s3, ...
    Valor de retorno: nÃºmero de NUEVO equiv. clases en 'stnt'.
*/
int division_clase_equiv(char stnt[][estados+1],
    int i1, /* indice de  'i1'-th clase equiv */
    int i2, /* indice del vectorequivalente para 'i1'-th class */
    int n,  /* numero de entradas en 'stnt' */
    int n_afd)  /* nÃºmero de entradas afd de origen */
{
    char *anterior=stnt[i1], *vec=stnt[i2];
    int i, n2, flag=0;
    char sig_estado[estados][estados+1];   /* max. 'n' sub clases */
    for (i=0; i < estados; i++) sig_estado[i][0] = '\0';
    for (i=0; vec[i]; i++)
        agregar_ch(sig_estado[vec[i]-'0'], anterior[i]);
    for (i=0, n2=n; i < n_afd; i++) {
        if (sig_estado[i][0]) {
            if (!flag) { 
                strcpy(stnt[i1], sig_estado[i]);
                flag = 1;   /* sobrescribir clase principal */
            } else  /* nuevo estado se agrega en 'stnt' */
                strcpy(stnt[n2++], sig_estado[i]);
        }
    }
    ordenar(stnt, n2); /* ordenar clases equivalentes */
    return n2;  /* numero de nuevos estados(clases equivalentes) */
}
/*
clases equivalentes estan segmentadas y obtienen una nueva clase equivalente
*/
int establecer_nueva_clase_equiv(char stnt[][estados+1], int n,int newafd[][simbolos], int n_sym, int n_afd)
{
    int i, j, k;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n_sym; j++) {
            k = newafd[i][j]-'A';   /* indice del vector equivalente */
            if (k >= n)  /* clase equivalente 'i' debe ser segmentado */
                return division_clase_equiv(stnt, i, k, n, n_afd);
        }
    }
    return n;
}
void imprimir_clases(char stnt[][estados+1], int n)
{
    int i;
    printf("\nClases equivalentes ==>");
    for (i = 0; i < n; i++)
        printf(" %d:[%s]", i, stnt[i]);
    printf("\n");
}
/*
    minimizacion de estados del afd: 'afd' --> 'newafd'
    Valor de retorno: numero de estados del afd.
*/
int afd_optimizado(
    int afd[][simbolos], /* tabla de transicion del afd */
    int n_afd,  /* numero de estados del afd */
    int n_sym, 
    char *final,   /* estados de aceptacion del afd */
    char stnt[][estados+1],  /* nombre de la tabla de estados */
    int newafd[][simbolos])  /* tabla del afd reducida */
{
    char nextstate[estados+1];
    int n;  /* cantidad de nuevos estados del afd*/
    int n2; 
    n = clase_init_equiv(stnt, n_afd, final);
    while (1) {
        imprimir_clases(stnt, n);
        n2 = obtener_afd_optimizado(stnt, n, afd, n_sym, newafd);
        if (n != n2)
            n = establecer_nueva_clase_equiv(stnt, n, newafd, n_sym, n_afd);
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
    char stnt[][estados+1],  /* tabla de estados  */
    int n)  /* numero de estados en 'stnt' */
{
    int i;
    for (i = 0; i < n; i++)
        if (es_sub(anteriores, stnt[i])) *nuevos++ = i+'A';
    *nuevos++ = '\0';
}
int main()
{
    cargar_tabla();
    imprimir_tabla_afd(afdtab, n_afd_estados, n_simbolos, afd_final);
    n_optafd_estados = afd_optimizado(afdtab, n_afd_estados,n_simbolos, afd_final, nombre_estados, Optafd);
    nuevos_aceptados(nuevo_final, afd_final, nombre_estados, n_optafd_estados);
    imprimir_tabla_afd(Optafd, n_optafd_estados, n_simbolos, nuevo_final);
}