# >>>>> classe coloredPrintRGB --------------------------------------------------------------------------------------
class coloredPrintRGB:
    """ Classe coloredPrintRGB : Usando sequencias de escape para imprimir colorido no print do console
            E possivel mudar a cor do texto assim como a cor de fundo do console."""
#... coloredPrintRGB
    def __init__(self,string,textColor=[0,0,0],backgroundColor=[255,255,255]):
        self.textColor = textColor ; self.backgroundColor = backgroundColor ; self.string = string ; self.default() ;
#... coloredPrintRGB    
    def __update_string(self): 
        """ atualiza a string de cor """
        self.__retSTR = self.__ces(self.backgroundColor,1)+self.__ces(self.textColor,0)+self.string+self.__default
#... coloredPrintRGB
    def __ces(self,LIST_COLOR,SWITCH_WORD2BACK=0): # shorthando for color escape sequence
        """ constroi a sequencia de escape para print colorido """
        # responsabilidades < __ces < coloredPrintRGB
        str_aux = str(LIST_COLOR[0]) + ";" + str(LIST_COLOR[1]) + ";" + str(LIST_COLOR[2]) + "m"
        if   SWITCH_WORD2BACK==0: return "\033[38;2;" + str_aux # sequencia para cor da letra  
        elif SWITCH_WORD2BACK==1: return "\033[48;2;" + str_aux # sequencia para cor do fundo
#... coloredPrintRGB
    def default(self,textColor=[0,0,0],backgroundColor=[255,255,255]):
        """ Configura o estado inicial e chama a atualizacao __act da string colorida """
        self.__default = self.__ces(textColor,0)+self.__ces(backgroundColor,1) ; self.__update_string() ;
#... coloredPrintRGB    
    def returnString(self): return self.__retSTR
    def printString(self): print(self.__retSTR)
#... coloredPrintRGB    
    def rangerPrint(self,number,maxNumber,iniColor,endColor,returnString=False):
        """ metodo [ coloredPrintRGB.rangerPrint(number,maxNumber,iniColor,endColor,returnString=False) ] 
            1) Retorna um print colorido de acordo com um gradiente de cor
            2) a razao number/maxNumber diz qual cor do gradiente ira ser retornado
            3) iniColor eh a cor inicial do gradiente, quando number = 0
            4) endColor eh a cor final do gradiente, quando number==maxNumber
            5) iniColor e endColor podem receber parametros string 'r','b','g'
            6) o metodo altera parametros do objeto e nao retorna nada, caso queira retorno ...
            ... faca returnString=True. """
        # imports < rangerPrint < coloredPrintRGB
        from math import floor as fl ; p = float(number)/maxNumber ; 
        # subrotinas        < rangerPrint < coloredPrintRGB
#... ... rangerPrint < coloredPrintRGB        
        def subrotina_comb_cor(): # combinacao linear de cor RGB (1-p){cor inicial} + p{cor final} = 255
            if   iniColor=='r': self.textColor[0] = fl(255*(1-p))
            elif iniColor=='g': self.textColor[1] = fl(255*(1-p))
            elif iniColor=='b': self.textColor[2] = fl(255*(1-p))
            if   endColor=='r': self.textColor[0] = fl(255*p)
            elif endColor=='g': self.textColor[1] = fl(255*p)
            elif endColor=='b': self.textColor[2] = fl(255*p)        
        # responsabilidades < rangerPrint < coloredPrintRGB
        subrotina_comb_cor() ; self.__update_string() ; self.printString() ;
        if returnString: return self.__retSTR
# >>>>> classe generalizada textInterface ---------------------------------------------------------------------
class textInterface():
    """ Classe para Controlar uma Interface Baseada em Input em uma Caixa de Texto, Voce digita comandos 
        dentro da caixa de texto e a interface deve responder de acordo com os comandos. Baseado em widgets do
        ipywidgets e usando o ambiente jupyter de computacao cientifica """
#... textInterface    
    def builder(self):
        """ Evite Raidar!!! construtor de widget 
            1) Widget Superior construido por upper_builder
            2) Textarea construido dentro desta rotina
            3) Widget Inferior construido por lower_builder """
#... ... builder < textInterface
        # responsabilidade [ imports ] < builder < textInterface
        from IPython.display import display, clear_output
        import ipywidgets as wdg
#... ... builder < textInterface
        # responsabilidade widget < builder < textInterface
        MAIN_TEXT = wdg.Textarea() ; 
        MAIN_TEXT.width = self.main_text_area_width ; MAIN_TEXT.height = self.main_text_area_height
#... ... builder < textInterface        
        # responsabilidade binding < builder < textInterface
        MAIN_TEXT.observe(self.commands,'value')
        # finalizacao < builder < textInterface
#... ... builder < textInterface        
        self.widget = wdg.VBox([ 
                                    self.upper_builder(), 
                                    MAIN_TEXT,
                                    self.lower_builder()
                                                        ])
        return self.widget    
#... textInterface
    def __init__(self,ARQUIVOSAVE=None):
        self.widget = None # Armazena a referencia do widget construido
        self.arquivoSave = ARQUIVOSAVE
        self.main_text_area_width = '450px'
        self.main_text_area_height = '200px'
#... textInterface        
    def save(self):
        """ Precisa de Override, rotina para salvar informacoes """
        pass
#... textInterface    
    def load(self):
        """ Precisa de Override, rotina para carregar informacoes de acordo com o save """
        pass
#... textInterface
    def reset_save(self):
        """ Precisa de Override, rotina para apagar o arquivo save """
        pass
#... textInterface    
    def upper_builder(self):
        """ Precisa de Override, constroi widget acima da caixa de texto """
        import ipywidgets as wdg
        return wdg.VBox()
#... textInterface        
    def lower_builder(self):
        """ Precisa de Override, constroi widget abaixo da caixa de texto """
        import ipywidgets as wdg
        return wdg.VBox()
#... textInterface    
    def commands(self,change):
        """ Precisa de Override, handle observer de comandos dentro do MAIN_TEXT que eh um widget Textarea no builder """
        from IPython.display import display, clear_output
        clear_output()
        print(change['new'])
#... textInterface
    def printDir():
        for i in dir(textInterface):
            if i[0]!='_':print(i)
# >>>>> Classe Dialetica Socratica --------------------------------------------------------------------------------------
class dialSocrates(textInterface):
#... dialSocrates
    def __init__(self,inp=None,arq_save=None):
        textInterface.__init__(self,arq_save)
        if inp==None:
            self.DICT = {'<b> Dialética Socrática : </b> Raiz dos Problemas':{}}
            self.CURR_DICT = self.DICT['<b> Dialética Socrática : </b> Raiz dos Problemas']
            self.PATH = ['<b> Dialética Socrática : </b> Raiz dos Problemas']
        else:
            print(inp.topicoPrincipal)
            self.DICT = {'<b> Dialética Socrática : </b>'+inp.topicoPrincipal :{}}
            self.CURR_DICT = self.DICT['<b> Dialética Socrática : </b>'+inp.topicoPrincipal]
            self.PATH = ['<b> Dialética Socrática : </b>'+inp.topicoPrincipal]            
        self.old_key = None
        self.guardaProblema = True
        self.level = 0
        self.digestor = inp
        if self.load()==None: self.save()
        self.main_text_area_width = '700px'
        self.main_text_area_height = '70px'
#... dialSocrates        
    def save(self):
        if self.digestor==None:
            fhandle = open('socr/'+self.arquivoSave,'w')
            fhandle.write(str(self.DICT))
            fhandle.close()
        else:
            fhandle = open('socr/'+self.digestor.arquivoSave+'_socr','w')
            fhandle.write(str(self.DICT))
            fhandle.close()
#... dialSocrates          
    def load(self):
        from ast import literal_eval
        try:
            if self.digestor!=None:
                fhandle = open('socr/'+self.digestor.arquivoSave+'_socr','r')
                self.DICT = literal_eval(fhandle.read())
                self.CURR_DICT = self.DICT['<b> Dialética Socrática : </b>'+self.digestor.topicoPrincipal]
                self.PATH = ['<b> Dialética Socrática : </b>'+self.digestor.topicoPrincipal]
            else:
                fhandle = open('socr/'+self.arquivoSave,'r')
                self.DICT = literal_eval(fhandle.read())
                self.CURR_DICT = self.DICT['<b> Dialética Socrática : </b> Raiz dos Problemas']
                self.PATH = ['<b> Dialética Socrática : </b> Raiz dos Problemas']                
        except:
            PRINT = coloredPrintRGB(string=" Não Há Arquivo de Dialética ",textColor=[0,245,0],backgroundColor=[0,0,0])
            PRINT.printString()
            return None
    def reset_save(self):
        try:
            import os
            old_dir = os.getcwd()
            os.chdir('socr')
            if self.digestor!=None:
                os.remove(self.digestor.arquivoSave+'_socr')
            else:
                os.remove(self.arquivoSave)
            os.chdir(old_dir)
            self.widget.close()
        except:
            PRINT = coloredPrintRGB(string=" Não Há Arquivo para Deletar ",textColor=[0,245,0],backgroundColor=[0,0,0])            
            PRINT.printString()
#... dialSocrates        
    def randomKey(self):
        from random import randint as rnd
        try:
            KEYS = list(self.CURR_DICT.keys())
            new_key = KEYS[rnd(0,len(KEYS)-1)]
            while new_key==self.old_key and len(KEYS)>1:
                new_key = KEYS[rnd(0,len(KEYS)-1)]
            self.old_key = new_key
            return self.old_key
        except:
            self.guardaProblema = True
            return 'Adicione Algo'
#... ... widgetsConst < dialSocrates        
    def upper_builder(self):
        import ipywidgets as wdg
        # widgets
        HTML = wdg.HTML()
        # handle
#... ... upper_builder < dialSocrates
        def handle_on_disp(ref):
            ref.value = ''+list(self.DICT.keys())[0]
        # binding
        HTML.on_displayed(handle_on_disp)
        return HTML
#... ... widgetsConst < dialSocrates            
    def lower_builder(self):
        import ipywidgets as wdg
        # widget
        HTML = wdg.HTML()
#... ... lower_builder < dialSocrates        
        def handle_on_disp(ref): 
            ref.value = self.randomKey()
            if ref.value!='Adicione Algo': self.guardaProblema = False
        HTML.on_displayed(handle_on_disp)
        return HTML
#... ... widgetsConst < dialSocrates            
    def commands(self,change):
        from IPython.display import display, clear_output
        # responsabilidade [ Capturar Mudanca ] < handle_obs <
        new_ = change['new'] ; old_ = change['old']
        # subrotinas < handle_obs
#... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates            
        def subrotina_nodo_pai():
            clear_output()
            # guarda
            if self.level == 0: return None
            self.guardaProblema = False          
            # responsabilidade
            self.CURR_DICT = self.DICT
#... ... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates                            
            for i in self.PATH[:-1]: self.CURR_DICT = self.CURR_DICT[i]
            #print(self.CURR_DICT)
            # responsabilidade
            self.PATH = self.PATH[:-1]
            # responsabilidade
            HTML_NODO = self.widget.children[0] ; HTML_NODO_CURR = self.widget.children[2] ; TEXTAREA = self.widget.children[1]           
            HTML_NODO.value = self.PATH[-1]
            HTML_NODO_CURR.value = self.randomKey()
            # responsabilidade
            TEXTAREA.value=''
            self.level -=1
            # responsabilidade
            idx = HTML_NODO.value.find('</b>')
            PRINT = coloredPrintRGB(string=" "+ HTML_NODO.value[idx+4:] +" ",textColor=[0,245,245],backgroundColor=[0,0,0])            
            PRINT.printString()              
#... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates                            
        def subrotina_nodo_filho():
            #clear_output()
            HTML_NODO = self.widget.children[0] ; HTML_NODO_CURR = self.widget.children[2] ; TEXTAREA = self.widget.children[1]            
            # guarda
#... ... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates                            
            if self.guardaProblema: return None
            # responsabilidade
            idx = HTML_NODO_CURR.value.find("</b>")
            PRINT = coloredPrintRGB(string=" "+HTML_NODO_CURR.value[idx+4:]+" ",textColor=[245,245,0],backgroundColor=[0,0,0])            
            PRINT.printString()        
            # responsabilidade
            self.PATH.append(self.old_key)
            self.CURR_DICT = self.CURR_DICT[self.old_key]
            # responsabilidade
           
            HTML_NODO.value = self.old_key
            HTML_NODO_CURR.value = self.randomKey()
            # responsabilidade 
            TEXTAREA.value=''
            self.level+=1
#... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates                            
        def subrotina_mudanca():
            TEXTAREA = self.widget.children[1] 
            #clear_output()
            #print('mudança')
            self.guardaProblema = False
            TEXTAREA.value=''
            HTML_NODO_CURR = self.widget.children[2] ;        
            HTML_NODO_CURR.value = self.randomKey()          
#... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates                            
        def subrotina_add_quest():
            #clear_output()
            TEXTAREA = self.widget.children[1]  
            PRINT = coloredPrintRGB(string=" Questionamento : "+TEXTAREA.value[:-1]+" ?",textColor=[0,245,0],backgroundColor=[0,0,0])            
            PRINT.printString()             
            # responsabilidade
            if self.level>0:
                self.CURR_DICT.update({ '<b>Sub-Pergunta : </b>'+TEXTAREA.value : { } })
            else:
                self.CURR_DICT.update({ '<b>Pergunta : </b>'+TEXTAREA.value : { } })
            # finalizacao
            TEXTAREA.value=''
            self.save()
            HTML_NODO_CURR = self.widget.children[2] ;        
            HTML_NODO_CURR.value = self.randomKey()
            self.guardaProblema=False
#... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates                            
        def subrotina_add_ans():
            #clear_output()
            TEXTAREA = self.widget.children[1]
            PRINT = coloredPrintRGB(string=" Possivel Resposta : "+TEXTAREA.value[:-1]+" !",textColor=[245,245,245],backgroundColor=[0,0,0])            
            PRINT.printString()            
            self.CURR_DICT.update({ '<b>Possível Resposta : </b>'+TEXTAREA.value : {  } })
            TEXTAREA.value=''
            HTML_NODO_CURR = self.widget.children[2] ;        
            HTML_NODO_CURR.value = self.randomKey()            
            self.save()
            self.guardaProblema=False
#... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates                            
        def subrotina_all_keys():
            #clear_output()
            count = 1
            for i in list(self.CURR_DICT.keys()):
                idx = i.find('</b>')
                pr = coloredPrintRGB(string=str(count)+") "+i[idx+4:]+" ",textColor=[122,255,155],backgroundColor=[0,0,0])
                pr.printString()
                count+=1
            TEXTAREA = self.widget.children[1]
            TEXTAREA.value=''
#... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates                                            
        def subrotina_all_path():
            count = 1
            for i in self.PATH[:-1]:
                idx = i.find('</b>')
                pr = coloredPrintRGB(string=str(count)+") "+i[idx+4:]+" ",textColor=[122,245,245],backgroundColor=[0,0,0])
                pr.printString()
                count+=1
            i = self.PATH[-1] ; idx = i.find('</b>')
            pr = coloredPrintRGB(" Pergunta Atual : "+i[idx+4:]+" ",textColor=[245,245,122],backgroundColor=[0,0,0])
            pr.printString()
            TEXTAREA = self.widget.children[1]
            TEXTAREA.value=''
#... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates                                            
        def subrotina_current():
            clear_output()
            PR = coloredPrintRGB(
                string=" Caminho Dialético de Perguntas e Respostas ".center(70,"-"),
                textColor=[255,255,255],
                backgroundColor=[0,0,0]) ; PR.printString()
            subrotina_all_path() ; 
            PR = coloredPrintRGB(
                string=" Perguntas e Respostas Subjacentes a Pergunta Atual ".center(70,"-"),
                textColor=[255,255,255],
                backgroundColor=[0,0,0]) ; PR.printString()            
            subrotina_all_keys()
#... ... ... handle_obs_TEXTAREA < widgetsConst < dialSocrates                                            
        def subrotina_help():
            PRT = """
    ------------------------------------------------------------------------------------
    Interface de Dialética Socrática
    ------------------------------------------------------------------------------------
    A dialética socrática tem dois tempos distintos, o primeiro tempo é a ironia em que 
        sócrates esgotava o interlocutor com perguntas até que ele se declarasse
        ignorante, somente assim ele poderia alcançar a verdadeira sabedoria.
    O segundo tempo do diálogo socrático corresponde a maiêutica em que próprio 
        interlocutor auxiliado por sócrates seria responsável por achar as respostas
        para as perguntas.
    Nesta interface não há estes dois tempos, e também não há duas entidades conscientes.
        O que se espera que seja feito é uma espécie de diálogo de você com você mesmo
        alternando entre o papel de questionador e propositor, você deve definir os tempos 
        do diálogo socrático ao seu gosto, mas é sugerido que se esforce nas perguntas antes 
        de tentar responder e que toda resposta não é definitiva, mas sim uma proposição.
    O nome é uma homenagem a Sócrates, mas o método não constitui um diálogo propriamente 
        dito, você deve arquirir as habilidades de questionar e de propor as soluções.
    Esta interface permite que você possa organizar suas ideias, herda os benefícios do
        paradigma de dividir para conquistar, organiza as proposições de maneira hierárquica,
        e simula um diálogo. O que é interessante para autodidatas.
    ------------------------------------------------------------------------------------
    digite @help para mostrar ajuda
    digite @exit para sair e salvar
    digite @clear para resetar o output
    digite @save para salvar
    digite @load para carregar arquivo salvo
    digite @reset save para apagar o arquivo save
    ------------------------------------------------------------------------------------
    digite @all para saber de tudo que foi perguntado ou respondido do assunto corrente
    digite @path para saber o caminho até a pergunta atual
    digite @current para colocar o caminho e os nodos subjacentes do problema atual
    digite > para mudar o assunto corrente para uma subpergunta ou uma resposta
    digite < para voltar ao assunto anterior
    digite = para mudar a subpergunta ou a resposta em destaque
    digite uma pergunta seguido de ? para adicionar uma pergunta ao assunto corrente
    digite uma proposição seguido de ! para adicionar uma proposição ao assunto corrente
            """
            print(PRT)
            
        TEXTAREA = self.widget.children[1] 
        # responsabilidade [ Crivo ] < handle_obs
        if   old_+'>'==new_: subrotina_nodo_filho() 
        elif old_+'<'==new_: subrotina_nodo_pai()
        elif old_+'='==new_: subrotina_mudanca()
        elif old_+'?'==new_: subrotina_add_quest()
        elif old_+'!'==new_: subrotina_add_ans()
        elif       '@save'==new_: 
            self.save() ; TEXTAREA.value=''
        elif       '@load'==new_: 
            self.load() ; TEXTAREA.value=''
        elif '@reset save'==new_:
            self.reset_save() ; TEXTAREA.value=''
        elif '@exit'==new_: 
            self.widget.close()
            self.save()
        elif '@clear'==new_: 
            clear_output() ; TEXTAREA.value=''
        elif '@all'==new_: subrotina_all_keys()
        elif '@help'==new_: subrotina_help()
        elif '@path'==new_: subrotina_all_path()
        elif '@current'==new_: subrotina_current()
# >>>>> play_audio : funcao avulsa  --------------------------------------------------------------------------------------
def play_audio():
    import ipywidgets as wdg ; from IPython.display import display, clear_output, Audio ; import os
    # widget
    old_dir = os.getcwd() ; os.chdir(old_dir+'\\audio')
    OBJ = wdg.Dropdown(options=os.listdir()) ; OBJ.button_style='' ; os.chdir(old_dir)
    BUT = wdg.Button(description='Play')
    H = wdg.HBox([ OBJ, BUT ])
    # handle
    def handle(ref): clear_output() ; display(Audio(filename='audio\\'+OBJ.value, autoplay=True) )
    # binding e display
    BUT.on_click(handle) ; display(H)
# >>>>> classe theoDigestor < textInterface ---------------------------------------------------------------------
class theoDigestor(textInterface):
    """ Subclasse de textInterface, auxiliar no estudo de teorias/livros/artigos/etc. Baseado em widgets do
        ipywidgets e usando o ambiente jupyter de computacao cientifica """
#... digestor   
    def estudo(self,NIVEL=None):
        """ metodo para iniciar rotina de estudo, imports : numpy.random, IPython.display, ipywidgets """
        # imports          < estudo < digestor
        from numpy.random import randint as rnd ; from IPython.display import clear_output, display ; import ipywidgets as wdg ;        
        # subrotinas       < estudo < digestor        
#... ... estudo < digestor        
        def subrotina_print_pratoVazio():
            self.update_refeicao('ESTUDO VAZIO')
            print('digite @set mode span para selecionar modo expansao de inventario ou')
            print('\tdigite uma informação seguida de ponto de interrogação para adicionar \n\tinformação no modo normal.')  
#... ... estudo < digestor            
        def subrotina_print_pratoUnitario():
            print('digite @set mode span para selecionar modo expansao de inventario ou')
            print('\tdigite uma informação seguida de ponto de interrogação para adicionar \n\tinformação no modo normal.')        
        # responsabilidade < estudo < digestor
        self.load() ;
        # responsabilidade < estudo < digestor
        if   len(self.refeicao)==0 : subrotina_print_pratoVazio() 
        elif len(self.refeicao)==1 : subrotina_print_pratoUnitario()  
        # responsabilidade < estudo < digestor
        if NIVEL!=None: self.pontuacao = NIVEL ;
        if self.progresso(self.pontuacao)==-1: return None # significa que todas as informacoes estao com pontuacao acima
        # retorno final    < estudo < digestor
        display(self.builder()) # usa o criador de widgets para iniciar a interface de estudo        
#... theoDigestor   
    def builder(self):
        """ Evite Raidar!!! construtor de widget 
            1) Widget Superior construido por upper_builder
            2) Textarea construido dentro desta rotina
            3) Widget Inferior construido por lower_builder """
#... ... builder < theoDigestor
        # responsabilidade [ imports ] < builder < theoDigestor
        from IPython.display import display, clear_output
        import ipywidgets as wdg
#... ... builder < theoDigestor
        # responsabilidade widget < builder < theoDigestor
        MAIN_TEXT = wdg.Textarea() ; 
        MAIN_TEXT.width = self.main_text_area_width ; MAIN_TEXT.height = self.main_text_area_height
#... ... builder < theoDigestor        
        # responsabilidade widget [ botoes imagens ]< builder < theoDigestor
#... ... builder < theoDigestor        
        IMAGE_BUTTON_bookmark = wdg.Button(
                                    description = 'Bookmark',
                                    width='80px',
                                    height='70px',
                                    button_style='warning'
                                )
#... ... builder < theoDigestor
        IMAGE_good = wdg.Button(
                                    description = 'Good',
                                    width='60px',
                                    height='70px',
                                    button_style = 'success'
                                )
#... ... builder < theoDigestor                
        IMAGE_bad = wdg.Button(
                                    description = 'Bad',
                                    width='60px',
                                    height='70px',
                                    button_style = 'danger'
                                )                
#... ... builder < theoDigestor       
        # responsabilidade binding < builder < theoDigestor
        MAIN_TEXT.observe(self.commands,'value')
        # finalizacao < builder < theoDigestor
#... ... builder < theoDigestor   
        self.widget = wdg.VBox([ 
                                    self.upper_builder(), 
                                    wdg.HBox( [MAIN_TEXT, wdg.VBox([ 
                                                    IMAGE_BUTTON_bookmark , 
                                                    IMAGE_good,
                                                    IMAGE_bad
                                                                    ]) ] ),
                                    self.lower_builder()
                                                        ])
#... ... handles < builder < theoDigestor
        def handle_bookmark(ref2):
            TEXT = wdg.Text()
            link_handle = wdg.widgets.jslink( (TEXT,'value') , (self.widget.children[1].children[0], 'value') )
            BUTT = wdg.Button(description='Enviar')
            V = wdg.HBox([ TEXT, BUTT ])
#... ... ... set_last_page < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            def handle(ref):
                try:
                    if TEXT.value[-1]=='!':
                        self.last_page = TEXT.value[:-1]
                    else:    
                        self.last_page = TEXT.value
                    self.save_parameters()
                    link_handle.unlink()
                    V.close()
                except:
                    link_handle.unlink()
                    V.close()
#... ... ... set_last_page < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
            def handle_TEXT(change):
                new_ = change['new'] ; old_ = change['old']
                if old_+'!'==new_:
                    handle(None)
#... ... ... set_last_page < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
            def handle_ondisp(ref):
                if self.last_page!=None:
                    ref.value = self.last_page
            BUTT.on_click(handle)
            TEXT.observe(handle_TEXT,names='value')
            TEXT.on_displayed(handle_ondisp)
            display(V)
#... ... handles < builder < theoDigestor
        def handle_good(ref):
            """ subrotina resposta a reacao positiva em relacao a pergunta, responsavel por renovar o INPUT.old_question, 
            chamar o gerador de nova pergunta, atualizar a pergunta e incrementar o nivel da refeicao """
            # guardas [ Inicio de Programa ] < subrotina_react_Positivo <
            if self.initStateFlag==True:
                #subrotina_clearText(change)
                return None
            # guardas [ No Modo Invocacao ] < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG
            if self.mode_state=='invoc': 
                #subrotina_clearText(change)
                return None

            # subrotinas < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG
#... ... ... subrotina_react_Positivo < wdg_BrainWasher < creatorWDG              
            def sub2rotina_react_Positivo_Defalt():
                """ reacao normal de digitacao + """
                clear_output()
                self.old_question,idx = self.geradorPerguntas()
                # guardas [ Modo Adicao em Inventario ] < subrotina_react_Positivo
                if self.mode_expansion_state=='add' and  self.mode_state=='expansion_mode':
                    #subrotina_clearText(change)
                    return None
                self.widget.children[0].children[4].value = '<br> '+self.old_question+' ?<br>'
                if idx!=None: self.refeicao[self.old_question] += 1        
    #... ... ... subrotina_react_Positivo < wdg_BrainWasher < creatorWDG                    
            def sub2rotina_react_Positivo_Expansion():
                """ reacao de digitacao + condicionado ao modo expansao """
    #... ... ... ... sub2rotina_react_Positivo_Expansion < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG             
                if   self.mode_expansion_state=='add': # acho que pode tirar
                    self.widget.children[0].children[4].value = '<br> '+'<b>Modo Expansão : Adicione Informações</b>'+' <br>'
    #... ... ... ... sub2rotina_react_Positivo_Expansion < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG            
                elif self.mode_expansion_state=='inv':
                    clear_output()
                    self.old_question,idx = self.geradorPerguntas()
                    # guardas [ Modo Adicao em Inventario ] < subrotina_react_Positivo
                    if self.mode_expansion_state=='add' and  self.mode_state=='expansion_mode':
                        #subrotina_clearText(change)
                        return None
                    self.widget.children[0].children[4].value = '<br> '+self.old_question+' ?<br>'
    #... ... ... ... ... sub2rotina_react_Positivo_Expansion < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG                    
                    if idx!=None: self.refeicao[self.old_question] += 1
                    if   self.mode_inv_count <= self.mode_inv_max:
                        self.mode_inv_count += 1
                    else                                           :
                        self.mode_expansion_state='add' ; self.mode_inv_count=0
            # responsabilidades < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG
            if   self.mode_state=='default'       : sub2rotina_react_Positivo_Defalt()
            elif self.mode_state=='expansion_mode': sub2rotina_react_Positivo_Expansion()
            # retaguarda < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG
            if self.mode_expansion_state=='add': return None # estranho, acho que n precisa            
            self.progresso(self.pontuacao) # verificar se esta chamando algo
#... ... handles < builder < theoDigestor
        def handle_bad(ref):
            """ subrotina resposta a reacao negativa em relacao a pergunta, responsavel por aumentar o estomago, 
            chamar o gerador de pergunta, dizer se o estomago esta cheio, atualizar o INPUT.old_question,
            decrentar o nivel em menos 1"""
            # guardas [ Inicio de Programa ] < subrotina_react_Positivo <
            if self.initStateFlag==True:
                #subrotina_clearText(change)
                return None            
            # guardas < subrotina_react_Negativo < wdg_BrainWasher < creatorWDG
            if self.mode_state=='invoc': 
                #subrotina_clearText(change)
                return None 
               
            # sub2rotinas < subrotina_react_Negativo < wdg_BrainWasher < creatorWDG
#... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG
            def sub2rotina_reac_neg_default():
                clear_output()
                PERGUNTA,idx = self.geradorPerguntas()
                # guardas [ Modo Adicao em Inventario ] < subrotina_react_Positivo
                if self.mode_expansion_state=='add' and  self.mode_state=='expansion_mode':
                    #subrotina_clearText(change)
                    return None 
                self.widget.children[0].children[4].value = '<br> '+PERGUNTA+' ?<br>'
                if self.flagEstomago==False and self.old_question!=None:
                    print(self.old_question,'foi adicionado ao estomago')
                    self.Estomago.append(self.old_question)
                    #self.objwdg_BrainWasher.children[5].border = 'blue'
                if len(self.Estomago)>=self.tamanhoEstomago: 
                    self.flagEstomago=True
                    #self.objwdg_BrainWasher.children[5].border='solid blue'
                if idx!=None: 
                    try:
                        self.refeicao[self.old_question] -= 1
                    except:
                        pass
                self.old_question = PERGUNTA
#... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG                
            def sub2rotina_reac_neg_expansion():
                # -------------
                
                # -------------
                if self.mode_expansion_state=='add':
                    self.widget.children[0].children[4].value = '<br> '+'<b>Modo Expansão : Adicione Informações</b>'+' <br>'
                elif self.mode_expansion_state=='inv':
                    clear_output()
                    PERGUNTA,idx = self.geradorPerguntas()
                    # guardas [ Modo Adicao em Inventario ] < subrotina_react_Positivo
                    if self.mode_expansion_state=='add' and  self.mode_state=='expansion_mode':
                        #subrotina_clearText(change)
                        return None 
                    self.widget.children[0].children[4].value = '<br> '+PERGUNTA+' ?<br>'
#... ... ... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG                     
                    if self.flagEstomago==False and self.old_question!=None: 
                        print(self.old_question,'foi adicionado ao estomago')
                        self.Estomago.append(self.old_question)
                        #self.widget.children[0].children[5].border = 'blue'
#... ... ... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG                
                    if len(self.Estomago)>=self.tamanhoEstomago: 
                        self.flagEstomago=True
                        #self.objwdg_BrainWasher.children[5].border='solid blue'
#... ... ... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG                
                    if idx!=None: 
                        try:
                            self.refeicao[self.old_question] -= 1
                        except:
                            pass
                    self.old_question = PERGUNTA
                    if self.mode_inv_count <= self.mode_inv_max:
                        self.mode_inv_count += 1
                    else:
                        self.mode_expansion_state='add'
                        self.mode_inv_count=0            
#... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG             
            # responsabilidade < subrotina_react_Negativo < wdg_BrainWasher < creatorWDG             
            if   self.mode_state=='default'       : sub2rotina_reac_neg_default()           
            elif self.mode_state=='expansion_mode': sub2rotina_reac_neg_expansion()
            # retaguarda < subrotina_react_Negativo < wdg_BrainWasher < creatorWDG
            if self.mode_expansion_state=='add': return None            
            self.progresso(self.pontuacao)
            
#... ... wdg_BrainWasher < creatorWDG        
        def handle_TEXT_AREA_ondisplay(ref):
            # subrotinas
            def subrotina_set_mode_exp():
                clear_output() ; self.mode_state='expansion_mode' ; self.mode_expansion_state='add'
                self.save_parameters()
                self.widget.children[0].children[4].value = '<br> '+'<b>Modo Expansão Selecionado : Adicione Informações</b>'+' <br>'
            def subrotina_set_mode_invoc():
                # responsabilidade [ cria o botao ] < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
                BUTTON_clock = self.wdg_Clock()
                # responsabilidade [ configura o standby ] < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
                self.mode_state = 'invoc'
                # return final < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
                self.widget.children[0].children[4].value = '<br> <b>Modo Invocação Selecionado : Inicie a Invocação </b><br>'
                display(BUTTON_clock)    
            # responsabilidades
            if self.mode_state=='invoc'           : subrotina_set_mode_invoc()
            elif self.mode_state=='expansion_mode': subrotina_set_mode_exp()            

            # finalizacao < subrotina_react_Negativo < wdg_BrainWasher < creatorWDG
        
#... ... binding < builder < theoDigestor
        IMAGE_BUTTON_bookmark.on_click(handle_bookmark)
        IMAGE_good.on_click(handle_good)
        IMAGE_bad.on_click(handle_bad)
        return self.widget    
#... theoDigestor
    def __init__(self,arquivosave=None,inventario="""""",separador=';', exitmode=None):
        textInterface.__init__(self,ARQUIVOSAVE=arquivosave)
        self.main_text_area_height = '220px' ; 
        self.main_text_area_width = '470px'
        self.initStateFlag = True
        self.socratesFlag = False
#... __init__ < digestor        
        def subrotina_initAtr_modeInvoc():
            #self.mode_state = 'invocacao'
            #self.mode_invoc_time_count = 0
            self.mode_invoc_time_countMax = 12*60 # secs
            self.mode_invoc_dict = {}
            self.mode_invoc_pressClock = False
            if    self.mode_state=='invoc':
                self.old_mode_invoc = input(' selecione o modo que ira alternar o modo de invocação : default, expansion_mode ').strip()
            else: 
                self.old_mode_invoc = self.mode_state
            self.mode_invoc_record = None
#... __init__ < digestor            
        def subrotina_initAtr_modeExpansion():
            self.mode_state = 'default' ; 
            self.mode_expansion_state = 'add' 
            self.mode_add_count = 0     ; self.mode_add_max = 5 
            self.mode_inv_count = 0     ; self.mode_inv_max = 3*self.mode_add_max            
#... __init__ < digestor            
        def subrotina_initAtr_principais():
            self.refeicao = {} ; 
            self.arquivoSave = arquivosave ; self.separador = separador; self.update_refeicao(inventario) ; 
            self.topicoPrincipal = ''      ; self.palavrasChave = ''    ; self.fontes = ''   ;
            self.numRepeticoes = 35        ; self.tamanhoEstomago = 4   ; self.pontuacao = 0 ; 
            self.pesoEstomago = 2          ; self.printNiveis = 6       ; self.exit_mode = exitmode ;
            self.last_page = None ;
            self.ans_refeicao = {} ;
#... __init__ < digestor            
        def subrotina_initVar_Estomago():
            self.flagEstomago = False ; self.Estomago = [] ; self.countEstomago = 0
#... __init__ < digestor            
        def subrotina_initVar_Counting():
            self.index = 0 ; self.flagEND = False       
#... __init__ < digestor            
        def subrotina_initOld_Keepers():
            self.saveStatus = None    ; self.old_question = None ; self.old_version = None
#... __init__ < digestor            
        def subrotina_helpers():
            self.STR_help0 = """
    --------------------------------------------------------------------------------------------
    Caso tenha iniciado o programa selecione um modo de estudo:                                 
        @set mode span   : estudo alternado entre expansão de inventario e modo normal          
        @set mode estudo : estudo normal                                                        
        @set mode invoc  : estudo com modo de invocação                                         
    Mais informações nos outros botões                                                          
    --------------------------------------------------------------------------------------------
    digite @help para mostrar novamente a ajuda                                                 
    digite @config para visualizar e modificar configuracoes                                    
    digite @progress para mostrar o progresso do estudo                                         
    digite @remain para mostrar quantas repeticoes ainda faltam                                 
    digite @size para saber a quantidade de informacoes do inventario                           
    digite @last page para saber o conteudo salvo no marcador de pagina                         
    digite @bookmark para saber o conteudo salvo no marcador de pagina                          
    digite @pomo para ativar um countdown (pomodoro) em minutos                                 
    digite @socrates para ativar a interface dialetica socrática, digite @help                  
    digite @record para ver a quantidade de invocações no modo invocação                        
    --------------------------------------------------------------------------------------------
    digite + para selecionar opção de acerto                                                    
    digite - para selecionar opção de erro                                                      
    digite ! para adicionar informacoes no modo invocacao                                       
    digite ? para adicionar informacoes no inventario de estudo                                 
    --------------------------------------------------------------------------------------------
    digite @config para configurar parametros                                                   
    digite @set mode span para ativar o modo de expansao de inventario                          
    digite @set mode estudo para retornar o modo default                                        
    digite @set mode invoc para ativar o modo invocativo                                        
    digite @set last page para entrar com o marcador de pagina e clique enviar                  
    --------------------------------------------------------------------------------------------
    digite @clear para apagar o conteudo da caixa de texto                                      
    digite @stop para parar o estudo e salvar                                                   
    digite @exit para sair e salvar configuracoes                                               
    digite @reset save para resetar o arquivo save e parar o estudo                             
    digite @restart para iniciar um novo estudo                                                 
    digite @load parameters para carregar configuracoes salvas                                  
    digite @save parameters para salvar configuracoes                                           
    --------------------------------------------------------------------------------------------
    digite @python module para adicionar no inventario os conteudos internos de um modulo python
        atenção que ele apagua o conteúdo anterior                                              """
            
            
            self.STR_help1 = """
    ------------------------------------------------------------------------------------------------------
    MOTIVAÇÃO DE INTERFACE                                                                                
    ------------------------------------------------------------------------------------------------------
    A interação com os recursos do programa é majoritariamente por comandos inseridos na caixa de texto.  
                                                                                                          
    Justificativas :                                                                                      
    1) Apertar botões com o mouse gasta tempo físico e torna menos dinâmico o estudo.                     
    2) Este programa tem como uma das finalidades o aprendizado de computação, o uso do ambiente jupyter e
        a linguagem python é consistente com esse objetivo, pois permite o acesso ao código, fácil        
        compreensão e modificação.                                                                        
    3) Para programar o hardware de input ideal ainda é o teclado.                                        
                                                                                                          
    Por isso os únicos botões são para envio de informações e botões de ajuda.                            
                                                                                                          
    ------------------------------------------------------------------------------------------------------
    DESCRIÇÃO DE INTERFACE                                                                                
    ------------------------------------------------------------------------------------------------------
    1) Nome da Teoria, Fontes, Palavras-Chave                                                             
                                                                                                          
    Estes podem ser editados digitando @set char na caixa de texto presente na interface.                 
    Palavras-Chave podem ser adicionadas com o comando @add keyword.                                      
    As palavras-chave são importantes para o modo invocação.                                              
                                                                                                          
    2) Pergunta / MENSAGEM                                                                                
                                                                                                          
    Quando não tem uma mensagem explícita ele é uma pergunta selecionada aleatoriamente.                  
    Quando está no modo pergunta ele seleciona aleatoriamente uma informação registrada caso você saiba a 
        resposta precisa da informação (fórmula precisa, descrição precisa) então digite (+) na caixa de  
        texto, caso contrário digite (-)                                                                  
                                                                                                          
    3) Caixa de Texto                                                                                     
                                                                                                          
    A caixa de texto é o principal meio de interação com os recursos deste programa,                      
    Para adicionar informações a serem selecionadas digite o nome da informação seguido de ponto de       
        interrogação.                                                                                     
                                                                                                          
    No modo invocação digitar o nome de uma informação seguido de ! irá associar a informação a           
        palavra-chave, digitar = irá selecionar aleatoriamente uma palavra-chave.                         
                                                                                                          
    ------------------------------------------------------------------------------------------------------
    MODO DEFAULT                                                                                          
    ------------------------------------------------------------------------------------------------------
    Ativado explicitamente com o comando @set mode default                                                
                                                                                                          
    Este é o modo padrão de estudo, consiste em selecionar aleatoriamente nomes de informações salvas por 
        exemplo, nomes de teoremas, nomes de definições, propriedades.                                    
    Quando selecionado uma pergunta você tem as opções de digitar + ou - de acordo com a sua lembraça do  
        conteúdo preciso, isso irá aumentar ou diminuir a pontuação associada a informação.               
    O objetivo do estudo é preservar uma topologia uniforme entre informações, por isso é utilizado um    
        gerador aleatório uniforme para selecionar os conteúdos.                                          
    A topologia uniforme é compatível com a aplicação de uma teoria, para exposição é mais interessante   
        uma topologia linear, como no aprendizado de uma música.                                          
    Quando o parâmetro NIVEL do estudo é aumentado na prática é como se estivesse sendo feito um estudo   
        repetitivo.                                                                                       
                                                                                                          
    ------------------------------------------------------------------------------------------------------
    MODO EXPANSÃO                                                                                         
    ------------------------------------------------------------------------------------------------------
    Ativado explicitamente com o comando @set mode expansion                                              
                                                                                                          
    Este é o melhor modo quando está iniciando o estudo de uma teoria, ele alterna entre uma etapa de     
        adição de conteúdo e outra etapa que corresponde ao estudo normal.                                
                                                                                                          
    ------------------------------------------------------------------------------------------------------
    MODO INVOCAÇÃO                                                                                        
    ------------------------------------------------------------------------------------------------------
    Ativado explicitamente com o comando @set mode invoc                                                  
                                                                                                          
    Este tem como objetivo avaliar a quantidade de informações que você consegue resgatar da memória      
        estimulado por uma palavra-chave ou pelo tópico principal do estudo.                              
    Para iniciar efetivamente a contagem de tempo você deve apertar o botão azul (configurado para        
        terminar em 12 minutos). Depois de terminado ele irá salvar a quantidade de informações que você  
        consegui lembrar.                                                                                 
    As informações são adicionadas com sua descrição seguida de ! na caixa de texto.                      
    As informações não precisam ter nomes idênticos as informações do modo default, podem também ser      
        informações oriundas de outras fontes, o objetivo é lembrar conteúdos associados.                 """
            
            
            self.STR_help2 = """
    ------------------------------------------------------------------------------------------------------
    SUGESTÃO DE FORMATO DE INFORMAÇÃO                                                                     
    ------------------------------------------------------------------------------------------------------
    A formatação de uma informação adicionada no inventário de informações é livre, apenas deve terminar  
        com ponto de interrogação para o programa inserir na rotina de estudos.                           
                                                                                                          
    Entretanto recomendo que seja inserido algumas informações, abaixo o formato recomendado:             
                                                                                                          
    nome_da_informação ABREVIATURA_DE_FONTE pg NUMERO_DA_PAGINA                                           
                                                                                                          
    Teorema de Catheodory AGF pg 231                                                                      
                                                                                                          
    É preciso ter um nome descritivo ou um nome formal da informação, deve ter uma abraviatura da fonte   
        desta informação e deve ter a página da fonte utilizada.                                          
                                                                                                          
    As abreviaturas devem estar na descrição das fontes. Caso não esteja então digite @set char.          
                                                                                                          
    ------------------------------------------------------------------------------------------------------
    RECURSOS AUXILIARES DE ESTUDO                                                                         
    ------------------------------------------------------------------------------------------------------
    É interessante você ter um caderno ou algum espaço para escrever o conteúdo preciso das informações, o
        objetivo é a partir do nome da informação resgatar o conteúdo preciso, pois o nome da informação  
        em geral é mais fácil de gravar que uma fórmula.                                                  
    É interessante você ter um formulário ou um arquivo com as respostas certas das informações.          
    É interessante que você verbalize o nome do conteúdo e suas formulações precisas para aumentar o      
        CONTRASTE entre as informações.                                                                   
                                                                                                          
    ------------------------------------------------------------------------------------------------------
    PARADIGMAS DE MEMORIZAÇÃO                                                                             
    ------------------------------------------------------------------------------------------------------
    1) Não existe raciocínio sem memorização.                                                             
                                                                                                          
    2) Teorias racionais fazem uso de informações fáceis de memorizar, por conta da ordem por conta da    
        intuição, por conta de padrões, entretanto teorias racionais dependem da memorização.             
                                                                                                          
    3) Já não existe teorias exclusivamente racionais, sempre haverá informações importantes que não são  
        intuitivas e precisam ser tratadas com paradigmas de memorização.                                 
                                                                                                          
    4) O problema de resgatar informações complicadas pode ser visto como um processo de raciocínio...    
                                                                                                          
    Vamos definir raciocínio como o processo de ligar uma informação a outra através de informações       
        intermediárias.                                                                                   
    No resgate de informação complicada da memória queremos obter uma informação precisa através de um    
        nome ou de uma abstração, em geral informações complicadas não podem ser resgatadas imediatamente,
        por isso temos um processo em que partes menores da informação (mais fáceis de lembrar) ou versões
        mais simples da informação, ou mesmo abstrações da informação devem estimular em um processo      
        construtivo o resgate da informação complicada, no meio do caminho julgando as informações        
        erradas e que não fazem sentido.                                                                  
    Esse processo é como se fosse um raciocínio em que informações mais fáceis de lembrar estimula a      
        memória de versões mais refinadas da informação. Mas não é um raciocínio de implicação, nem de    
        causa e efeito.                                                                                   
                                                                                                          
    5) Caso uma informação esteja difícil de memorizar, decomponha esta informação em subinformações. Os  
        matemáticos em geral constroem teoremas agregando muitas informações, isso é extremamente         
        antiracional, as informações devem ser decompostas e nomeadas para serem facilmente acessadas,    
        ou as informações devem preservar ordem e padrões que justifiquem a ausência de nomes.            
                                                                                                          
    6) A velocidade de raciocínio tem dois fatores importantes, o tempo de resgate de informações da      
        memória e o tempo de ajustar as informações para obter uma conclusão de um problema. Assim como   
        em um computador o seu desempenho depende da velocidade de processamento assim como a velocidade  
        de acesso da memória e do disco rígido, ambos devem ser levados em conta.                         
                                                                                                          
    7) A hipótese essencial do método é considerar que os nomes das informaçãos são mais fáceis de        
        gravar que seu conteúdo preciso, entretanto para resover problemas dificilmente é suficiente      
        apenas uma informação. A invocação consiste na etapa de invocar várias informações associadas     
        a uma palavra-chave e simula um dos processos necessários para resolução de provas sem consulta.  """
        subrotina_helpers()
        subrotina_initAtr_principais()
        self.update_refKeys_restr(None)
        subrotina_initOld_Keepers()
        subrotina_initVar_Estomago()
        subrotina_initVar_Counting()
        subrotina_initAtr_modeExpansion()
        subrotina_initAtr_modeInvoc()
        self.load_parameters()
#... digestor
    def update_invoc_keywords(self,UPDATE=None):
        """ atualiza as palavras chave para a invocacao em self.mode_invoc_dict """
        # subrotinas < update_invoc_keywords < digestor
#... ... update_invoc_keywords < digestor        
        def subrotina_atualiza_dict():
            # responsabilidade [ verifica update ] < subrotina_atualiza_dict < update_invoc_keywords < digestor
            if   UPDATE==None       : # inicializa mode_invoc_dict
                self.mode_invoc_dict.update({ i : [] for i in self.palavrasChave.split(',') })
            elif type(UPDATE)==dict : # adiciona pelo update palavras-chave
                self.mode_invoc_dict.update(UPDATE)
            elif type(UPDATE)==list : # adiciona pelo update caso seja uma lista
                self.mode_invoc_dict.update({ i : [] for i in UPDATE })
#... ... update_invoc_keywords < digestor                    
        def subrotina_criaKeysList():
            self.mode_invoc_keys = list(self.mode_invoc_dict.keys())
        # responsabilidade [ Existencia de Palavras-Chave ] < update_invoc_keywords < digestor
        if   self.palavrasChave=='': 
            self.mode_invoc_dict = None
            return None
        else                      : 
            subrotina_atualiza_dict()
            subrotina_criaKeysList()
#... digestor
    def refeicao_py_module(self,STRING_MODULE,BOOL_PRINT=False):
        """ a partir do nome do modulo retorna um dicionario no formato refeicao com seu conteudo """
        IMPORT = __import__(STRING_MODULE) ; DICT = {}
        for i in IMPORT.__dir__(): 
            if i[0]!='_':
                if BOOL_PRINT: print(i)
                DICT.update({i:0})
        return DICT
#... digestor
    def geradorKeyWords(self):
        """ seleciona aleatoriamente (uniformemente) uma palavra chave """
        # modificacao : seleciona um caso diferente 29062019
        from numpy.random import randint as rnd ;
        # responsabilidade [ Achar Novo Keyword ] < geradorKeyWords < digestor
        NEW_KEYWORD = self.mode_invoc_keys[rnd(0,len(self.mode_invoc_keys))]
        try:
            while NEW_KEYWORD==self.old_invoc_key:
                NEW_KEYWORD = self.mode_invoc_keys[rnd(0,len(self.mode_invoc_keys))]
        except: 
            pass
        # responsabilidade [ Atualizar KeyWord ] < geradorKeyWords < digestor
        self.old_invoc_key = NEW_KEYWORD
        return self.old_invoc_key
#... digestor
    def invocResult(self):
        """ faz a contagem das invocacoes """
        print(' Resultado do Inventario :', self.topicoPrincipal,'\n')
        countTotal = 0
        for i in self.mode_invoc_keys:
            L = len(self.mode_invoc_dict[i])
            print(i.lstrip()+' : ', L )
            countTotal+=L
        print('\n','Contagem Total de Invocações :', countTotal)
        return countTotal
#... digestor
    def invoc_printKeyContent(self,KEY):
        """ imprime o conteudo associado a chave gerada no HTML de pergunta """
        from IPython.display import clear_output
        clear_output()
        print('* ITENS ASSOCIADOS A PALAVRA CHAVE :',KEY,'\n')
        for i in self.mode_invoc_dict[KEY]: print(i.lstrip())
#... digestor
    def invoc_updateDictByStr(self,STRING):
        """ adiciona informacoes no inventario de invocacao associado a chave antiga """
        self.mode_invoc_dict[self.old_invoc_key]+=STRING[:-1].split(self.separador)    
#... theoDigestor    
    def save(self):
        """ salva a refeicao no self.arquivoSave"""
        # imports    < save < digestor
        import os
        # subrotinas < save < digestor
        def subrotina_criarArquivoSave():
            for i in os.listdir(): print(i)
            self.arquivoSave=str(input('Nome do Arquivo : '))          
        # responsabilidade < save < digestor
        self.saveStatus='salvo' ;
        if self.arquivoSave==None : subrotina_criarArquivoSave()
        # retorno final < save < digestor
        fhandle = open(self.arquivoSave,'w') ; fhandle.write(str(self.refeicao)) ; fhandle.close() ;
#... digestor
    def save_parameters(self):
        # imports          < save_parameters < digestor
        import os
        # responsabilidade [ EXITMODE ] < save_parameters < digestor
        if self.exit_mode==None: MODESTATE = self.mode_state
        else                   : MODESTATE = self.exit_mode
        # responsabilidade < save_parameters < digestor
        try   : os.mkdir('config')
        except: pass
        DIC_SAVE_PARAMETERS = { 
                                'topicoPrincipal' : self.topicoPrincipal,
                                'palavrasChave' : self.palavrasChave,
                                'fontes' : self.fontes,
                                'numRepeticoes' : self.numRepeticoes,
                                'tamanhoEstomago' : self.tamanhoEstomago,
                                'pontuacao' : self.pontuacao,
                                'pesoEstomago' : self.pesoEstomago,
                                'printNiveis' : self.printNiveis,
                                'mode_state' : MODESTATE,
                                'mode_expansion_state' : self.mode_expansion_state,
                                'last page' : self.last_page,
                                'mode_invoc_time_countMax' : self.mode_invoc_time_countMax,
                                'record' : self.mode_invoc_record
                              }
        # return < save_parameters < digestor
        fhandle = open('config/'+self.arquivoSave+'_config','w') ; fhandle.write(str(DIC_SAVE_PARAMETERS) ) ; fhandle.close()
        print('Parametros de Configuracao Salvos em Arquivo :','config/'+self.arquivoSave+'_config')        
#... theoDigestor 
    def load(self):
        """ carrega a refeicao """
        # imports          < load < digestor
        import os, ast
        # subrotinas       < load < digestor
#... ... load < digestor        
        def subrotina_criaNomeArquivoSave():
            for i in DIRETORIO: print(i)
            self.arquivoSave = str(input('Nome do Arquivo : '))            
#... ... load < digestor            
        def subrotina_existeNomeArquivoSave():
            if subrotina_isinDir(): 
                NOME = str(self.arquivoSave)
            else: 
                self.save()
                NOME = str(self.arquivoSave)
#... ... load < digestor                        
        def subrotina_negIsInDir():
            B=False
            for i in DIRETORIO:
                if i==self.arquivoSave:
                    B=True
                    break
            return not B
#... ... load < digestor                
        def subrotina_isNonEmptyDict():
            self.refeicao = READ ; self.update_refKeys_restr()
#... ... load < digestor             
        def subrotina_isNonEmptyList():
            self.refeicao = { i[0] : i[1] for i in READ } ; self.update_refKeys_restr()        
        # responsabilidade < load < digestor
        DIRETORIO = os.listdir()
        # responsabilidade [ Ler Refeicao ] < load < digestor
        if self.arquivoSave==None: subrotina_criaNomeArquivoSave()
        if subrotina_negIsInDir(): self.save()
        self.saveStatus='Carregado' ; fhandle = open(self.arquivoSave,'r') ; 
        READ = ast.literal_eval( fhandle.read() ) ; fhandle.close()
        # responsabilidade [ Interpretar Refeicao ] < load < digestor
        if len(READ)<=0 or len(READ)==None: self.save()
        elif type(READ)==dict: subrotina_isNonEmptyDict()
        elif type(READ)==list: subrotina_isNonEmptyList()
#... digestor        
    def load_parameters(self):
        import ast
        try:
            fhandle = open('config/'+self.arquivoSave+'_config','r')
            DIC_SAVE_PARAMETERS       = ast.literal_eval( fhandle.read() )
            self.topicoPrincipal      = DIC_SAVE_PARAMETERS['topicoPrincipal']
            self.palavrasChave        = DIC_SAVE_PARAMETERS['palavrasChave']
            self.fontes               = DIC_SAVE_PARAMETERS['fontes']
            self.numRepeticoes        = DIC_SAVE_PARAMETERS['numRepeticoes']
            self.tamanhoEstomago      = DIC_SAVE_PARAMETERS['tamanhoEstomago']
            self.pontuacao            = DIC_SAVE_PARAMETERS['pontuacao']
            self.pesoEstomago         = DIC_SAVE_PARAMETERS['pesoEstomago']
            self.printNiveis          = DIC_SAVE_PARAMETERS['printNiveis']
            self.mode_state           = DIC_SAVE_PARAMETERS['mode_state']
            self.mode_expansion_state = DIC_SAVE_PARAMETERS['mode_expansion_state']
            self.last_page            = DIC_SAVE_PARAMETERS['last page']
            self.mode_invoc_record    = DIC_SAVE_PARAMETERS['record']
            self.mode_invoc_time_countMax = DIC_SAVE_PARAMETERS['mode_invoc_time_countMax']
            fhandle.close()
            print('Parametros de Configuracao Carregados')
        except:
            print('Nao ha arquivo de configuracao\n')
            print('Usando configuracao default ou definida em celula\n')
            return -1            
#... theoDigestor
    def reset_save(self):
        """ apaga o arquivo save de refeicao """
        import os ; old_dir = os.getcwd()
        try    : os.remove(self.arquivoSave)
        except : print('arquivo save não encontrado')
        try    : 
            os.chdir(old_dir+'\\config') ; os.remove(self.arquivoSave+'_config') ; os.chdir(old_dir)
        except : print('arquivo de configuracao nao encontrado')
        try    :
            os.chdir(old_dir+'\\ans') ; os.remove(self.arquivoSave+'_ans') ; os.chdir(old_dir)
        except : print('arquivo de resposta nao encontrado')
#... digestor
    def update_refKeys_restr(self,PONTUACAO=None):
        """ atualiza as chaves self.refKeys_restr que tem pontuacao menor ou igual a self.pontuacao e que 
            ... precisam ser estudados e retorna o self.refKeys_restr """
        # subrotinas       < update_refKeys_restr < digestor 
#... ... update_refKeys_restr < digestor    
        def subrotina_refKeys_restr(P): 
            self.refKeys_restr = [ i for i in self.refeicao_keys_list if self.refeicao[i]<=P ]        
        # responsabilidade < update_refKeys_restr < digestor
        if self.arquivoSave==None: self.load() # acho que esta errado
        self.refeicao_keys_list = list(self.refeicao.keys()) ; # candidato a ser promovido a variavel privada
        # responsabilidade < update_refKeys_restr < digestor
        if PONTUACAO==None: subrotina_refKeys_restr(self.pontuacao)
        else:               subrotina_refKeys_restr(PONTUACAO)
        # retorno final    < update_refKeys_restr < digestor
        return self.refKeys_restr # candidato a ser promovido a variavel privada
#... digestor
    def update_refeicao(self,KEYLIST):
        """ entra uma lista de chaves (informacoes para adicionar) e retorna o numero de adicionados na self.refeicao,
            nao salva a refeicao no arquivoSave. """
        # subrotinas        < update_refeicao < digestor
        def subrotina_estudoVazio():
            if   self.topicoPrincipal!='': self.refeicao.update({ self.topicoPrincipal : 0 })
            else                         : self.refeicao.update({ 'Tópico Principal' : 0 })           
        # responsabilidades < update_refeicao < digestor
        if   type(KEYLIST)==list and len(KEYLIST)>0 : self.refeicao.update({key:0 for key in KEYLIST})
        elif       KEYLIST=='ESTUDO VAZIO'          : subrotina_estudoVazio()
        elif type(KEYLIST)==str                     : self.refeicao.update({ i : 0 for i in KEYLIST.split(self.separador) })
        # retorno final     < update_refeicao < digestor
        if KEYLIST!=None :return len(KEYLIST) # sera util para o expansion_mode  
#... digestor       
    def geradorPerguntas(self):
        """ gerador de perguntas """
        # imports    < geradorPerguntas < digestor
        from numpy.random import randint as rnd ;
        # subrotinas < geradorPerguntas < digestor
#... ... geradorPerguntas < digestor
        def subrotina_atividadeEstomacal():
            # responsabilidade < subrotina_atividadeEstomacal < geradorPerguntas < digestor
            print('DENTRO DO ESTOMAGO : Estudo Focado nos Erros')
            PERGUNTA = self.Estomago[rnd(0,len(self.Estomago))]
            # responsabilidade [ contagem do estomago ] < subrotina_atividadeEstomacal < geradorPerguntas < digestor
            self.countEstomago += 1
            if self.countEstomago>int(self.pesoEstomago*self.tamanhoEstomago):
                self.countEstomago=0 ; self.flagEstomago=False ; self.Estomago = []
            # responsabilidade [ contagem geral ] < subrotina_atividadeEstomacal < geradorPerguntas < digestor 
            self.index += 1
            if self.index > self.numRepeticoes: 
                self.index = 0 ; self.flagEND = True
            # retorno final < subrotina_atividadeEstomacal < geradorPerguntas < digestor
            return PERGUNTA,None
#... ... geradorPerguntas < digestor        
        def subrotina_atividadeNormal():
            # responsabilidade < subrotina_atividadeNormal < geradorPerguntas < digestor
            #print('FORA DO ESTOMAGO : Estudo Normal')
            # responsabilidade [ contagem ] < subrotina_atividadeNormal < geradorPerguntas < digestor
            self.index +=1
            if self.index > self.numRepeticoes:
                self.index = 0 ; self.flagEND = True
            # responsabilidade [ geracao de pergunta ] < subrotina_atividadeNormal < geradorPerguntas < digestor
            Idx = self.update_refKeys_restr() ; LenIdx = len(Idx) ; 
            if LenIdx>0: 
                X = rnd(0,LenIdx) ; Idx_X = Idx[X]            
                return Idx_X, X
            # returno final [ Apenas se Terminou o Estudo ] < subrotina_atividadeNormal < geradorPerguntas < digestor
            return subrotina_terminoEstudo()
#... ... geradorPerguntas < digestor        
        def subrotina_terminoEstudo():
            self.save()
            for i in range(self.printNiveis): self.progresso(i)            
            return 'ATENCAO O ESTUDO TERMINOU : USE O RESTART', None        
#... ... geradorPerguntas < digestor 
        # responsabilidade < geradorPerguntas < digestor
        if   self.flagEND      : return subrotina_terminoEstudo()
        elif self.flagEstomago : return subrotina_atividadeEstomacal()
        else                   : return subrotina_atividadeNormal()     
        # retorno final < geradorPerguntas <digestor
        print("ERRO : DEVERIA TER ENTRADO EM ALGUMA ROTINA")        
#... theoDigestor
    def upper_builder(self):
        """ Título da Rotina BrainWasher,
            Título da Teoria
                Fontes
                Palavras-Chave
            DISPLAY 1 """
        import ipywidgets as wdg
        HTML_TITLE = wdg.HTML('<h3>BrainWasher : Auxiliar de Estudo e Memorização</h3><hr>')
        HTML_NOME_DE_TEORIA = wdg.HTML('<h4>[ '+self.topicoPrincipal+' ]</h4>')
        HTML_FONTE = wdg.HTML('<b> Fontes : </b> { '+self.fontes+' }') ; HTML_FONTE.margin = '0px 0px 0px 35px'
        HTML_PALAVRAS_CHAVES = wdg.HTML('<b>Palavras-Chave :  </b>{ '+self.palavrasChave+' }') ; HTML_PALAVRAS_CHAVES.margin = '0px 0px 0px 35px'
        HTML_PERGUNTA = wdg.HTML(100*'-') # self.widget.children[0].children[4]
        return wdg.VBox([
                HTML_TITLE,
                HTML_NOME_DE_TEORIA,
                HTML_FONTE,
                HTML_PALAVRAS_CHAVES,
                HTML_PERGUNTA
            ])
#... theoDigestor     
    def lower_builder(self):
        """ Precisa de Override, constroi widget abaixo da caixa de texto """
        import ipywidgets as wdg
        from IPython.display import clear_output
        # widgets < wdg_BrainWasher < creatorWDG
        BUTTON_help = wdg.Button(description=' Help : Comandos ') ; BUTTON_help.button_style= 'danger' ;
        BUTTON_help_interface = wdg.Button(description=' Help : Interface ') ; 
        BUTTON_help_interface.button_style = 'success' ; 
        #BUTTON_help_interface.width = '300px'
        BUTTON_help_paradigmas = wdg.Button(description=' Help : Paradigmas ')
        BUTTON_help_paradigmas.button_style='info'
        HBOX_BUTT = wdg.HBox( [ BUTTON_help , BUTTON_help_interface , BUTTON_help_paradigmas ] )
#... ... wdg_BrainWasher < creatorWDG        
        def handle_BUTTON_help_paradigmas(ref):
            """ Acionado quando pressionado o botal help : paradigmas """
            clear_output()
            STR_PR = self.STR_help2
            CS = coloredPrintRGB(string=STR_PR,textColor=[0,255,0],backgroundColor=[0,0,0])
            CS.printString()            
#... ... wdg_BrainWasher < creatorWDG
        def handle_BUTTON_help_interface(ref):
            """ Acionado quando pressionado o botao help : interface """
            clear_output()
            STR_PR = self.STR_help1
            CS = coloredPrintRGB(string=STR_PR,textColor=[0,255,0],backgroundColor=[0,0,0])
            CS.printString()
#... ... wdg_BrainWasher < creatorWDG        
        def handle_BUTTON_help(ref): 
            clear_output()
            STR_help = self.STR_help0
            CS = coloredPrintRGB(string=STR_help,textColor=[0,255,0],backgroundColor=[0,0,0])
            CS.printString()
#... theoDigestor < binding
        BUTTON_help.on_click(handle_BUTTON_help)
        BUTTON_help_interface.on_click(handle_BUTTON_help_interface)
        BUTTON_help_paradigmas.on_click(handle_BUTTON_help_paradigmas)        
        return HBOX_BUTT
#... theoDigestor 
    def commands(self,change):
        """ Precisa de Override, handle observer de comandos dentro do MAIN_TEXT que eh um widget Textarea no builder """
        from IPython.display import display, clear_output
        import ipywidgets as wdg
#... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_clearText(C): C['owner'].value=''
#... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG        
        def try_substr(string,a,b):
            try   : 
                if   b=='all': return string[a:]
                elif a=='all': return string[:b]
                else         : return string[a:b]
            except: return None
                     
            
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_stop():
            clear_output()
            for i in range(self.printNiveis): self.progresso(i)                
            self.save()
            self.widget.close()
            #print('SALVO')
            try   : self.objwdg_Clock.close()
            except: pass
            try   : self.objwdg_Envio.close()
            except: pass                
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG     
        def subrotina_clear():
            clear_output()
            #print('CLEARING')
            subrotina_clearText(change)
            try:    self.objwdg_Envio.close()
            except: pass
            try:    self.objwdg_Pomodoro.close()
            except: pass
            try:    self.objwdg_Clock.close()
            except: pass
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG     
        def subrotina_help():
            clear_output()
            STR_help = self.STR_help0
            CS = coloredPrintRGB(string=STR_help,textColor=[0,255,0],backgroundColor=[0,0,0])
            CS.printString()
            subrotina_clearText(change)        
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG     
        def subrotina_progress():
            clear_output()
            for i in range(self.printNiveis): self.progresso(i)
            subrotina_clearText(change)        
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG 
        def subrotina_info():
            clear_output() ; self.printInfoConfig() ; subrotina_clearText(change)        
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                 
        def subrotina_restart():
            clear_output() ; self.flagEND=False ; self.index=0 ; subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG             
        def subrotina_reset_save():
            clear_output() ; self.reset_save() ; self.widget.close() ; subrotina_clearText(change)        
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG            
        def subrotina_info_add():
            if self.initStateFlag: return None
            # guardas < subrotina_info_add < handle_TEXT_ATEA < wdg_BrainWasher < creatorWDG
            if self.mode_state=='invoc': return None
            # responsabilidade < subrotina_info_add < handle_TEXT_ATEA < wdg_BrainWasher < creatorWDG
            clear_output()
            N = self.update_refeicao(old_.split(self.separador))
            self.update_refKeys_restr() ; self.save()
            if   self.mode_state=='expansion_mode' and self.mode_expansion_state=='add':
                print('Adicionado Informação em Inventário em Modo Expansão')
                if self.mode_add_count <= self.mode_add_max:
                    self.mode_add_count += N
                else:
                    self.mode_add_count = 0
                    self.mode_expansion_state = 'inv'
                    self.widget.children[0].children[4].value = '<br> '+'<b>Modo Estudo : Digite + ou -</b>'+' <br>'
            elif self.mode_state=='default':
                print('Adicionado Informação em Inventário em Modo Normal')
            else :
                print('Adicionado Informação em Inventário')
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
        def subrotina_disp_size():
            clear_output()
            print('Tamanho do Inventario :',len(self.refeicao.keys()))
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
        def subrotina_remain():
            # guarda < subrotina_remain < handle_TEXT_AREA < 
            if self.initStateFlag: return None
            clear_output()
            print(self.index-1,'estudos completos de um total de',self.numRepeticoes)   
            #print('Tamanho do Inventario : '+str(len(self.refeicao.keys()))+'\n')
            #print('Numero de Selecoes : '+str(self.numRepeticoes))
            #print('Quantidade de Estudos Atual :',self.index,'\n')
            print('Pontuação de Estudo : Pontuação Menor ou Igual a : ' +str(self.pontuacao))
            print('Tamanho Maximo do Estomago : '+str(self.tamanhoEstomago))
            print('Tamanho Atual do Estomago :',len(self.Estomago))
            #print('Arquivo Save :',self.arquivoSave)
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
        def subrotina_delete():
            # guardas < subrotina_delete < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
            if self.mode_state=='invoc': return None
            try:
                if self.mode_expansion_state=='add': return None
            except:
                pass
            # responsabilidade < subrotina_delete < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG 
            clear_output()
            print(self.old_question,'deletado')
            try:
                self.refeicao.pop(self.old_question) ; self.update_refKeys_restr() ; self.save()
            except:
                pass
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_load_parameters():
            clear_output() ; self.load_parameters() ; self.update_cabecalho_BrainWasher() ; subrotina_clearText(change)
            try   : self.objwdg_Envio.close()    
            except: pass
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
        def subrotina_save_parameters():
            clear_output() ; self.save_parameters() ; subrotina_clearText(change)
            try   : self.objwdg_EnvioEnvio.close()    
            except: pass
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
        def subrotina_exit_quit():
            clear_output() ; self.save_parameters()
            for i in range(self.printNiveis): self.progresso(i)                
            self.save()            
            try   : self.objwdg_Envio.close()
            except: pass
            try   : self.widget.close()
            except: pass
            try   : self.objwdg_Clock.close()
            except: pass
            try   : self.objwdg_Pomodoro.close()
            except: pass
            print('Programa Terminado com Sucesso')
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
        def subrotina_set_mode_exp():
            clear_output() ; self.mode_state='expansion_mode' ; self.mode_expansion_state='add' ; self.initStateFlag = False
            self.save_parameters()
            self.widget.children[0].children[4].value = '<br> '+'<b>Modo Expansão Selecionado</b>'+' <br>'
            try   : self.objwdg_Clock.close()
            except: pass                
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
        def subrotina_set_mode_default():
            clear_output()
            self.initStateFlag = False
            self.mode_state='default' ; self.mode_expansion_state='inv' ; self.save_parameters()
            self.widget.children[0].children[4].value = '<br> '+'<b>Modo Estudo Padrão : Digite + ou - ou Aperte os Botões [Good/Bad] </b>'+' <br>'
            try   : self.objwdg_Clock.close()
            except: pass                
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_set_mode_invoc():
            # responsabilidade [ cria o botao ] < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            BUTTON_clock = self.wdg_Clock()
            # responsabilidade [ configura o standby ] < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            self.mode_state = 'invoc' ; self.initStateFlag = False
            # return final < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            self.widget.children[0].children[4].value = '<br> <b>Modo Invocação Selecionado : Clique No Botão Abaixo </b><br>'
            display(BUTTON_clock)
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
        def subrotina_invoc_changeKey():
            if self.mode_invoc_pressClock == False: return None
            self.geradorKeyWords()
            self.invoc_printKeyContent(self.old_invoc_key)
            self.widget.children[0].children[4].value = '<br> '+'<b>Modo Invocação : Palavra-Chave : </b><br><br>'+ self.old_invoc_key +' <br>'                
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_invoc_add():
            if self.mode_invoc_pressClock == False: return None
            self.invoc_updateDictByStr(self.widget.children[1].children[0].value)
            self.invoc_printKeyContent(self.old_invoc_key)
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def set_last_page(ref2=None):
            TEXT = wdg.Text()
            link_handle = wdg.widgets.jslink( (TEXT,'value') , (self.widget.children[1].children[0], 'value') )
            BUTT = wdg.Button(description='Enviar')
            V = wdg.HBox([ TEXT, BUTT ])
#... ... ... set_last_page < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            def handle(ref):
                try:
                    if TEXT.value[-1]=='!':
                        self.last_page = TEXT.value[:-1]
                    else:    
                        self.last_page = TEXT.value
                    self.save_parameters()
                    link_handle.unlink()
                    V.close()
                except:
                    link_handle.unlink()
                    V.close()            
#... ... ... set_last_page < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
            def handle_TEXT(change):
                new_ = change['new'] ; old_ = change['old']
                if old_+'!'==new_:
                    handle(None)
#... ... ... set_last_page < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
            def handle_ondisp(ref):
                try:
                    ref.value = self.last_page
                except:
                    pass
            BUTT.on_click(handle)
            TEXT.observe(handle_TEXT,names='value')
            TEXT.on_displayed(handle_ondisp)
            display(V)
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_add_keyword():
            TEXT = wdg.Text() ; BUTT = wdg.Button(description='Enviar')
            V = wdg.HBox([ TEXT, BUTT ])
#... ... ... ... subrotina_add_keyword < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
            def handle(ref): 
                # guarda
                if TEXT.value=='': 
                    V.close() ; return None
                # responsabilidade
                self.palavrasChave += ','+TEXT.value ; V.close()
                self.save_parameters()
                subrotina_update_cabecalho_BrainWasher()
            BUTT.on_click(handle) ; display(V)
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_python_module():
            # responsabilidade [ widget button ] < subrotina_python_module < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            # widget construction
            BUTTON = wdg.Button(description='Enviar') ; TEXT = wdg.Text() ; HBOX = wdg.HBox( [ TEXT, BUTTON ] )
            # handles
#... ... ... ... subrotina_python_module < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            def handle(ref):
                try:
                    self.refeicao.update(self.refeicao_py_module(TEXT.value))
                    self.topicoPrincipal = 'Modulo Python : '+TEXT.value
                    #self.addFonte('Help Python') ; self.addFonte(',Google')
                    self.update_cabecalho_BrainWasher()
                except:
                    print(' Falha em Importacao de Modulo ')
                TEXT.close() ; BUTTON.close() ; HBOX.close()
            # event binding
            BUTTON.on_click(handle)
            # display
            display(HBOX)
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_pomodoro():
            subrotina_clearText(change)
            display(self.wdg_PomodoroButton(INPUT=self))
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_ans_description(STRING): 
            try   : self.ans_refeicao[ self.old_question ]['descr'] = STRING
            except: self.ans_refeicao.update({ self.old_question : { 'descr' : STRING , 'latex' : '', 'video' : '' } })
            print(self.old_question)
            subrotina_clearText(change)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG    
        def subrotina_ans_latex(STRING): pass
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG    
        def subrotina_ans_video(STRING): pass
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_socrates():
            subrotina_clearText(change)
            OBJ_SC = dialSocrates(inp=self) ; self.TEXT_SOCR = OBJ_SC.builder() ;
            display(self.TEXT_SOCR)
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG            
        def subrotina_last_page_print():
            CS = coloredPrintRGB(string=" Página Marcada : " + str(self.last_page) + " ", textColor=[0,255,0], backgroundColor=[0,0,0])
            CS.printString()
            #print(' Página Marcada : ',self.last_page)
            subrotina_clearText(change) 
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG           
        def subrotina_record():
            clear_output()
            CS = coloredPrintRGB(
                            string=" Recorde de Invocações Anterior : "+str(self.mode_invoc_record)+" ",
                            textColor = [ 0,255,0 ],
                            backgroundColor = [0,0,0]
                                    )
            CS.printString()
            subrotina_clearText(change)
#... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def subrotina_config():
            display(self.enviar_dados())
            subrotina_clearText(change)
#... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        def CORINGA(change): 
            print(change)
            pass
            
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
        def subrotina_react_Positivo():
            """ subrotina resposta a reacao positiva em relacao a pergunta, responsavel por renovar o INPUT.old_question, 
            chamar o gerador de nova pergunta, atualizar a pergunta e incrementar o nivel da refeicao """
            # guardas [ Inicio de Programa ] < subrotina_react_Positivo <
            if self.initStateFlag==True:
                #subrotina_clearText(change)
                return None
            # guardas [ No Modo Invocacao ] < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG
            if self.mode_state=='invoc': 
                #subrotina_clearText(change)
                return None

            # subrotinas < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG
#... ... ... subrotina_react_Positivo < wdg_BrainWasher < creatorWDG              
            def sub2rotina_react_Positivo_Defalt():
                """ reacao normal de digitacao + """
                clear_output()
                self.old_question,idx = self.geradorPerguntas()
                # guardas [ Modo Adicao em Inventario ] < subrotina_react_Positivo
                if self.mode_expansion_state=='add' and  self.mode_state=='expansion_mode':
                    #subrotina_clearText(change)
                    return None
                self.widget.children[0].children[4].value = '<br> '+self.old_question+' ?<br>'
                if idx!=None: self.refeicao[self.old_question] += 1
#... ... ... subrotina_react_Positivo < wdg_BrainWasher < creatorWDG                    
            def sub2rotina_react_Positivo_Expansion():
                """ reacao de digitacao + condicionado ao modo expansao """
#... ... ... ... sub2rotina_react_Positivo_Expansion < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG             
                if   self.mode_expansion_state=='add': # acho que pode tirar
                    self.widget.children[0].children[4].value = '<br> '+'<b>Modo Expansão : Adicione Informações</b>'+' <br>'
#... ... ... ... sub2rotina_react_Positivo_Expansion < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG            
                elif self.mode_expansion_state=='inv':
                    clear_output()
                    self.old_question,idx = self.geradorPerguntas()
                    # guardas [ Modo Adicao em Inventario ] < subrotina_react_Positivo
                    if self.mode_expansion_state=='add' and  self.mode_state=='expansion_mode':
                        #subrotina_clearText(change)
                        return None
                    self.widget.children[0].children[4].value = '<br> '+self.old_question+' ?<br>'
#... ... ... ... ... sub2rotina_react_Positivo_Expansion < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG                    
                    if idx!=None: self.refeicao[self.old_question] += 1
                    if   self.mode_inv_count <= self.mode_inv_max:
                        self.mode_inv_count += 1
                    else                                           :
                        self.mode_expansion_state='add' ; self.mode_inv_count=0
            # responsabilidades < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG
            if   self.mode_state=='default'       : sub2rotina_react_Positivo_Defalt()
            elif self.mode_state=='expansion_mode': sub2rotina_react_Positivo_Expansion()
            # retaguarda < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG
            if self.mode_expansion_state=='add': return None # estranho, acho que n precisa            
            self.progresso(self.pontuacao) # verificar se esta chamando algo

            # finalizacao < subrotina_react_Positivo < wdg_BrainWasher < creatorWDG
            #subrotina_clearText(change)
#... ... wdg_BrainWasher < creatorWDG        
        def subrotina_react_Negativo():
            """ subrotina resposta a reacao negativa em relacao a pergunta, responsavel por aumentar o estomago, 
            chamar o gerador de pergunta, dizer se o estomago esta cheio, atualizar o INPUT.old_question,
            decrentar o nivel em menos 1"""
            # guardas [ Inicio de Programa ] < subrotina_react_Positivo <
            if self.initStateFlag==True:
                #subrotina_clearText(change)
                return None            
            # guardas < subrotina_react_Negativo < wdg_BrainWasher < creatorWDG
            if self.mode_state=='invoc': 
                #subrotina_clearText(change)
                return None 
               
            # sub2rotinas < subrotina_react_Negativo < wdg_BrainWasher < creatorWDG
#... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG
            def sub2rotina_reac_neg_default():
                clear_output()
                PERGUNTA,idx = self.geradorPerguntas()
                # guardas [ Modo Adicao em Inventario ] < subrotina_react_Positivo
                if self.mode_expansion_state=='add' and  self.mode_state=='expansion_mode':
                    #subrotina_clearText(change)
                    return None 
                self.widget.children[0].children[4].value = '<br> '+PERGUNTA+' ?<br>'
                if self.flagEstomago==False and self.old_question!=None:
                    print(self.old_question,'foi adicionado ao estomago')
                    self.Estomago.append(self.old_question)
                    #self.objwdg_BrainWasher.children[5].border = 'blue'
                if len(self.Estomago)>=self.tamanhoEstomago: 
                    self.flagEstomago=True
                    #self.objwdg_BrainWasher.children[5].border='solid blue'
                if idx!=None: 
                    try:
                        self.refeicao[self.old_question] -= 1
                    except:
                        pass
                self.old_question = PERGUNTA
#... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG                
            def sub2rotina_reac_neg_expansion():
                # -------------
                
                # -------------
                if self.mode_expansion_state=='add':
                    self.widget.children[0].children[4].value = '<br> '+'<b>Modo Expansão : Adicione Informações</b>'+' <br>'
                elif self.mode_expansion_state=='inv':
                    clear_output()
                    PERGUNTA,idx = self.geradorPerguntas()
                    # guardas [ Modo Adicao em Inventario ] < subrotina_react_Positivo
                    if self.mode_expansion_state=='add' and  self.mode_state=='expansion_mode':
                        #subrotina_clearText(change)
                        return None 
                    self.widget.children[0].children[4].value = '<br> '+PERGUNTA+' ?<br>'
#... ... ... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG                     
                    if self.flagEstomago==False and self.old_question!=None: 
                        print(self.old_question,'foi adicionado ao estomago')
                        self.Estomago.append(self.old_question)
                        #self.widget.children[0].children[5].border = 'blue'
#... ... ... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG                
                    if len(self.Estomago)>=self.tamanhoEstomago: 
                        self.flagEstomago=True
                        #self.objwdg_BrainWasher.children[5].border='solid blue'
#... ... ... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG                
                    if idx!=None: 
                        try:
                            self.refeicao[self.old_question] -= 1
                        except:
                            pass
                    self.old_question = PERGUNTA
                    if self.mode_inv_count <= self.mode_inv_max:
                        self.mode_inv_count += 1
                    else:
                        self.mode_expansion_state='add'
                        self.mode_inv_count=0            
#... ... ... subrotina_react_Negativo < wdg_BrainWasher < creatorWDG             
            # responsabilidade < subrotina_react_Negativo < wdg_BrainWasher < creatorWDG             
            if   self.mode_state=='default'       : sub2rotina_reac_neg_default()           
            elif self.mode_state=='expansion_mode': sub2rotina_reac_neg_expansion()
            # retaguarda < subrotina_react_Negativo < wdg_BrainWasher < creatorWDG
            if self.mode_expansion_state=='add': return None            
            self.progresso(self.pontuacao)

            # finalizacao < subrotina_react_Negativo < wdg_BrainWasher < creatorWDG
            #subrotina_clearText(change)            
            
#... ... wdg_BrainWasher < creatorWDG        
            
            
#... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        # responsabilidade < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        old_ = change['old'] ; new_ = change['new']        
        #clear_output()
        
        if '@'==try_substr(new_,0,1):
            if 'CORINGA'==try_substr(new_,1,'all')   : CORINGA()
#... ... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            elif 'set'==try_substr(new_ ,1,4): # set class command
                if   'mode span'==try_substr(new_,5,'all')     : subrotina_set_mode_exp()
                elif 'mode estudo'==try_substr(new_,5,'all')     : subrotina_set_mode_default()
                elif 'mode invoc'==try_substr(new_,5,'all')     : subrotina_set_mode_invoc()
                elif 'bookmark'==try_substr(new_,5,'all') or 'last page'==try_substr(new_,5,'all') : set_last_page()
#... ... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                        
            elif 'python'==try_substr(new_,1,7): # python class command
                if   'module'==try_substr(new_,8,'all'): subrotina_python_module()
#... ... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                        
            elif 'ans'==try_substr(new_,1,4):
                # ---------------------------------------------
                if   'description'==try_substr(new_,5,16):
                    if   'END'==try_substr(new_,-3,'all'): subrotina_ans_description(try_substr(new_,16,-3))
                elif 'latex'==try_substr(new_,5,10)      : 
                    if   'END'==try_substr(new_,-3,'all'): subrotina_ans_latex(try_substr(new_,10,-3))                        
                elif 'video'==try_substr(new_,5,10)      :
                    if   'END'==try_substr(new_,-3,'all'): subrotina_ans_video(try_substr(new_,10,-3))
#... ... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                        
            elif 'ask desc'==try_substr(new_,1,'all'):
                try   : print(INPUT.ans_refeicao[INPUT.old_question]['descr'])
                except: print('EXCECAO')            
#... ... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                    
            elif 'ask latex'==try_substr(new_,1,'all'): pass
#... ... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG    
            elif 'ask video'==try_substr(new_,1,'all'): pass                
#... ... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG                
            elif 'config'==try_substr(new_,1,'all')  : subrotina_config()
            elif 'exit'==try_substr(new_,1,'all')    : subrotina_exit_quit()
            elif 'last page'==try_substr(new_,1,'all') or 'bookmark'==try_substr(new_,1,'all') : subrotina_last_page_print()
            elif 'clear'==try_substr(new_,1,'all')              : subrotina_clear()             
            elif 'help'==try_substr(new_,1,'all')               : subrotina_help()
            elif 'progress'==try_substr(new_,1,'all')                   : subrotina_progress()
            elif 'restart'==try_substr(new_,1,'all')                    : subrotina_restart()
            elif 'reset save'==try_substr(new_,1,'all')                 : subrotina_reset_save()
            elif 'size'==try_substr(new_,1,'all')                                     : subrotina_disp_size()
            elif 'remain'==try_substr(new_,1,'all')                                   : subrotina_remain()
            elif 'delete'==try_substr(new_,1,'all')                                   : subrotina_delete() # testar!!!!
            elif 'load parameters'==try_substr(new_,1,'all')                          : subrotina_load_parameters()
            elif 'save parameters'==try_substr(new_,1,'all')                          : subrotina_save_parameters()
            elif 'pomo'==try_substr(new_,1,'all')    : subrotina_pomodoro()
            elif 'socrates'==try_substr(new_,1,'all')    : subrotina_socrates()
            elif 'record'==try_substr(new_,1,'all') : subrotina_record()
#... ... ... handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
        elif old_+'+'==new_                               : subrotina_react_Positivo()
        elif old_+'-'==new_                               : subrotina_react_Negativo()                
        elif old_+'?'==new_                               : subrotina_info_add()
        elif self.mode_state=='invoc' and old_+'='==new_ : subrotina_invoc_changeKey()
        elif self.mode_state=='invoc' and old_+'!'==new_ : subrotina_invoc_add()            
        #print(change['new'])
#... ... binding < commands < theoDigestor



#... theoDigestor
    def printDir():
        for i in dir(textInterface):
            if i[0]!='_':print(i)
#... digestor       
    def progresso(self,Pontuacao):
        # subrotina < progresso < digestor
        def subrotina_prgstr(X,T):
            RN = round
            return " Nivel : "+str(Pontuacao)+" : ["+RN(42.*X/T)*"#"+RN(42.*(T-X)/T)*"-" +"] "+str(100.*X/T)+" % "        
        # responsabilidade < progresso < digestor
        Idx = self.update_refKeys_restr(Pontuacao) ; LenIdx = len(Idx) ; LenL = len(self.refeicao_keys_list)
        c = LenL-LenIdx; Prog = coloredPrintRGB(subrotina_prgstr(c,LenL)) ; Prog.backgroundColor = [0,0,0] ;
        # responsabilidade < progresso < digestor
        if LenIdx!=0: 
            Prog.rangerPrint(c,LenL,'r','g')
            return 0
        else:
            Prog.string = subrotina_prgstr(LenL,LenL) ; Prog.rangerPrint(LenL,LenL,'r','g')
            return -1
#... digestor         
    def update_cabecalho_BrainWasher(self):
        self.widget.children[0].children[1].value = '<h4>[ '+self.topicoPrincipal+' ]</h4>' ;
        self.widget.children[0].children[2].value = '<b> Fontes : </b> { '+self.fontes+' }' ;
        self.widget.children[0].children[2].margin = '0px 0px 0px 35px' ;
        self.widget.children[0].children[3].value = '<b>Palavras-Chave :  </b>{ '+self.palavrasChave+' }' ;
        self.widget.children[0].children[3].margin = '0px 0px 0px 35px'  
        self.save_parameters()
#... creatorWDG    
    def enviar_dados(self):
        # imports < enviar_dados < creatorWDG
        import ipywidgets as wdg
        from IPython.display import display,clear_output
        # responsabilidades < enviar_dados < creatorWDG
        self.load()
        self.progresso(self.pontuacao)        
        # widgets < enviar_dados < creatorWDG
        HTML = wdg.HTML('<br> <b>Configurações Gerais</b>')
        INT_TEXT_numRep = wdg.IntText(value=self.numRepeticoes) ; 
        INT_TEXT_tamEst = wdg.IntText(value=self.tamanhoEstomago) ; 
        FLOAT_TEXT_pesEst = wdg.FloatText(value=self.pesoEstomago) ;
        INT_TEXT_printNiveis = wdg.IntText(value=self.printNiveis) ;
        INT_TEXT_pontuacao = wdg.IntText(value=self.pontuacao) ; 
        TEXT_fontes = wdg.Text(value=self.fontes) ;
        TEXT_topicoPrincipal = wdg.Text(value=self.topicoPrincipal) ;
        TEXT_palavrasChave = wdg.Text(value=self.palavrasChave) ;
        HTML_expansion = wdg.HTML('<br><b>Configurações de Modo Expansão</b>')
        INT_TEXT_submode_add = wdg.IntText(value=self.mode_add_max)
        INT_TEXT_submode_inv = wdg.IntText(value=self.mode_inv_max)
        HTML_invoc = wdg.HTML('<br><b>Configurações de Modo Invocação</b>')
        FLOAT_TEXT_time = wdg.FloatText(value=self.mode_invoc_time_countMax)
        BUTTON_envio = wdg.Button(description=' ENVIAR DADOS ') ;
        BOX_envio = wdg.VBox( [ HTML,
                                wdg.HBox([ INT_TEXT_numRep, wdg.Label('Numero de Sorteios Maximo') ]), # BOX com os w's
                                wdg.HBox([ INT_TEXT_tamEst, wdg.Label('Numero de Reacoes Negativas Maxima') ]),
                                wdg.HBox([ FLOAT_TEXT_pesEst, wdg.Label('Peso de Repeticoes de Erros') ]),
                                wdg.HBox([ INT_TEXT_printNiveis, wdg.Label('Numero de Niveis Impressos') ]),
                                wdg.HBox([ TEXT_topicoPrincipal, wdg.Label('Topico Principal/Nome da Teoria')   ]),
                                wdg.HBox([ TEXT_fontes, wdg.Label('Fontes') ]),
                                wdg.HBox([ TEXT_palavrasChave, wdg.Label('Palavras-Chave') ]),
                                wdg.HBox([ INT_TEXT_pontuacao, wdg.Label('Nivel de Estudo/Pontuacao') ]) ,
                                HTML_expansion,
                                wdg.HBox([ INT_TEXT_submode_add , wdg.Label('Quantidade de Adições de Inventário') ]),
                                wdg.HBox([ INT_TEXT_submode_inv , wdg.Label('Quantidade de Repetições em Modo Estudo') ]),
                                HTML_invoc,
                                wdg.HBox([ FLOAT_TEXT_time , wdg.Label('Tempo de Contagem Regressiva (secs)') ])
                              ] )       
        # event_handles < enviar_dados < creatorWDG
        def handle_BUTTON_envio(ref):
            # responsabilidade < handle_BUTTON_envio < enviar_dados < creatorWDG
            self.numRepeticoes = INT_TEXT_numRep.value ; 
            self.tamanhoEstomago = INT_TEXT_tamEst.value ; 
            self.pesoEstomago = FLOAT_TEXT_pesEst.value ;
            self.printNiveis = INT_TEXT_printNiveis.value ; 
            self.pontuacao = INT_TEXT_pontuacao.value ;
            self.fontes = TEXT_fontes.value ;
            self.topicoPrincipal = TEXT_topicoPrincipal.value ;
            self.palavrasChave = TEXT_palavrasChave.value ;
            self.mode_add_max = INT_TEXT_submode_add.value ;
            self.mode_inv_max = INT_TEXT_submode_inv.value ;
            self.mode_invoc_time_countMax = FLOAT_TEXT_time.value ;
            # responsabilidade < handle_BUTTON_envio < enviar_dados < creatorWDG
            sp = ' ' ; clear_output() ;
            self.progresso(self.pontuacao) ; 
            #PALAVRA = coloredPrintRGB(25*sp+'ENVIADO '+25*sp,[0,255,0],[0,0,0]) ; PALAVRA.printString()
            # responsabilidade < handle_BUTTON_envio < enviar_dados < creatorWDG
            self.objwdg_Envio.close() ; self.objwdg_Envio = None
            # responsabilidade < handle_BUTTON_envio < enviar_dados < creatorWDG
            self.update_cabecalho_BrainWasher()
        # event binding < enviar_dados < creatorWDG
        BUTTON_envio.on_click(handle_BUTTON_envio)
        # retorno final < enviar_dados < creatorWDG
        self.objwdg_Envio = wdg.VBox([ BOX_envio, BUTTON_envio ])
        return self.objwdg_Envio    
#... creatorWDG
    def wdg_Clock(self):
        """ cria um botao relogio que inicia o modo inventario e faz uma contagem de tempo """
        # imports           < wdg_Clock < creatorWDG
        import ipywidgets as wdg ; import time ; from IPython.display import clear_output, display 
        # subrotinas        < wdg_Clock < creatorWDG
        def subrotina_diff_time(ASC1,ASC2):    
            return subrotina_getSecs(ASC2) - subrotina_getSecs(ASC1)
        def subrotina_getSecs(ASC):
            T1, T2, T3 = ASC.split(' ')[3].split(':')
            return int(T1)*360 + int(T2)*60 + int(T3)        
        # responsabilidade [ widget ] < wdg_Clock < creatorWDG
        # widget construction < responsabilidade [ widget ] < wdg_Clock < creatorWDG
        BUTTON_clock = wdg.Button(description=str(self.mode_invoc_time_countMax)+' secs')
        BUTTON_clock.button_style = 'info'
        # widget handles      < responsabilidade [ widget ] < wdg_Clock < creatorWDG
        def handle_BUTTON_clock(ref):
            # guarda < handle_BUTTON_clock < wdg_Clock < creatorWDG
            if self.mode_invoc_pressClock: return None
            # imports < handle_BUTTON_clock < wdg_Clock < creatorWDG
            import threading as thr
            # subrotinas < handle_BUTTON_clock < wdg_Clock < creatorWDG
            def subrotina_thread(ref):
                self.mode_invoc_pressClock = True
                countTime = 0
                finalTime = self.mode_invoc_time_countMax            
                while countTime<finalTime:
                    time.sleep(1)
                    ref.description = str( (finalTime - countTime) )+' secs'
                    countTime+=1
                ref.description = str(self.mode_invoc_time_countMax)+' secs'
                self.mode_state = self.old_mode_invoc
                if self.mode_state   == 'default':
                    self.widget.children[0].children[4].value = '<br> '+'<b>Modo Default</b>'+ '<br>'                
                elif self.mode_state == 'expansion_mode':
                    self.widget.children[0].children[4].value = '<br> '+'<b>Modo Expansão</b>'+ '<br>'                
                self.objwdg_Clock.close()
                self.mode_invoc_pressClock = False
                clear_output()
                RES_INV = self.invocResult()
                print(' Recorde Anterior: ',self.mode_invoc_record)
                try:
                    if RES_INV > self.mode_invoc_record : 
                        print(' Teve um Novo Recorde: ' , RES_INV) ; self.mode_invoc_record = RES_INV
                except:
                    self.mode_invoc_record = RES_INV
                self.save_parameters()
            # responsabilidade < handle_BUTTON_clock < wdg_Clock < creatorWDG
            self.update_invoc_keywords(None)
            self.geradorKeyWords()
            self.invoc_printKeyContent(self.old_invoc_key)
            sp = ' '
            self.widget.children[0].children[4].value = '<br> '+'<b>Modo Invocação : Palavra-Chave :</b> <br><br>'+ self.old_invoc_key +' <br>'
            # responsabilidade < handle_BUTTON_clock < wdg_Clock < creatorWDG
            thread = thr.Thread(target=subrotina_thread, args=(ref,))
            thread.start()    
        # widget binding      < responsabilidade [ widget ] < wdg_Clock < creatorWDG
        BUTTON_clock.on_click(handle_BUTTON_clock)
        # return            < wdg_Clock < creatorWDG
        self.objwdg_Clock = wdg.HBox([ BUTTON_clock, wdg.Label('Countdown : Clique para Inicio de Inventario') ])
        return self.objwdg_Clock

#... creatorWDG                
    def wdg_PomodoroButton(self,INPUT=None,PLAYAUDIO=False):
        import ipywidgets as wdg
        from IPython.display import clear_output
        # subrotinas < wdg_PomodoroButton < creatorWDG
        # responsabilidade [ widget ] < wdg_PomodoroButton < creatorWDG
        # widgets
        POMODORO = wdg.Button(description='POMODORO(minutos)')
        POMODORO.button_style = 'danger'
        POMODORO.width = '210px'
        TEXT = wdg.Text()
        # linking
        link_handle = wdg.widgets.jslink( (TEXT,'value') , (self.widget.children[1].children[0],'value') )
        V = wdg.HBox( [TEXT, POMODORO] )
        # handles
#... ... wdg_PomodoroButton < creatorWDG         
        def handle(ref):
            # imports < handle < wdg_PomodoroButton < creatorWDG
            import time ; import threading as thr
            from IPython.display import clear_output, Audio, display
            # subrotina < handle < wdg_PomodoroButton < creatorWDG
#... ... ... handle < wdg_PomodoroButton < creatorWDG            
            def subrotina_handle_thr(ref):
                TEXT.close()
                ref.button_style = '' ; ref.width = '452px'
                ref.on_click(idle)
                countTime = 0
#... ... ... ... handle < wdg_PomodoroButton < creatorWDG                            
                if TEXT.value=='': finalTime = 45
                else            : finalTime = float(TEXT.value)*60 # em minutos
#... ... ... ... handle < wdg_PomodoroButton < creatorWDG                                            
                while countTime<finalTime:
                    time.sleep(5)
                    ref.description = 'Pomodoro : '+str( (finalTime - countTime) )+' secs'
                    countTime+=5
                self.objwdg_Pomodoro.close()
                clear_output()
#... ... ... ... handle < wdg_PomodoroButton < creatorWDG                                            
                if INPUT!=None:
                    for i in range(10):
                        INPUT.progresso(i)
                    INPUT.save_parameters()
                    INPUT.save()
#... ... ... ... handle < wdg_PomodoroButton < creatorWDG                                                
                try: self.widget.close()
                except: pass
                try: self.objwdg_Envio.close()
                except: pass
                try: self.objwdg_Clock.close()
                except: pass
#... ... ... ... handle < wdg_PomodoroButton < creatorWDG
                if PLAYAUDIO: display(Audio(filename='audio/StrongHold.mp3',autoplay=True))
#... ... ... handle < wdg_PomodoroButton < creatorWDG
            THR = thr.Thread(target=subrotina_handle_thr, args=(ref,))
            link_handle.unlink()
            THR.start()
            
#... ... wdg_PomodoroButton < creatorWDG                                    
        def handle_obs_TEXT(change): 
            clear_output()
            print(change['new'],'minutos')
            new_ = change['new'] ; old_ = change['old']
            if old_+'!'==new_:
                TEXT.value = TEXT.value[:-1]
                handle(POMODORO)
        def idle(ref): pass
        # binding
        POMODORO.on_click(handle)
        TEXT.observe(handle_obs_TEXT,names='value')

        # finalizacao < wdg_PomodoroButton < creatorWDG
        self.objwdg_Pomodoro = V
        return self.objwdg_Pomodoro
# >>>>> classe digestor_InvEst < digestor
class digestor_InvEst(theoDigestor):
    """ Classe Derivada de Classe [ digestor ], comeca sempre no modo inventario, depois vai para o modo default """
    def __init__(self,INVENTARIO=None,ARQUIVOSAVE=None):
        self.mode_state = 'default'
        super(digestor_InvEst,self).__init__(inventario=INVENTARIO, separador=';',arquivosave=ARQUIVOSAVE, exitmode='invoc')
    def estudo(self,NIVEL=None):
        from IPython.display import display
        super(digestor_InvEst,self).estudo(NIVEL)
        def subrotina_set_mode_invoc():
            # responsabilidade [ cria o botao ] < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            BUTTON_clock = self.wdg_Clock()
            # responsabilidade [ configura o standby ] < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            self.mode_state = 'invoc' ; self.initStateFlag = False
            # return final < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            self.widget.children[0].children[4].value = '<br> <b>Modo Invocação Selecionado : Clique No Botão Abaixo </b><br>'
            display(BUTTON_clock)
        subrotina_set_mode_invoc()
# >>>>> classe digestor_InvExp < digestor
class digestor_InvExp(theoDigestor):
    """ Classe Derivada de Classe [ digestor ], comeca em modo inventario e depois em modo expansao """
    def __init__(self,INVENTARIO=None,ARQUIVOSAVE=None):
        super(digestor_InvExp,self).__init__(inventario=INVENTARIO, separador=';',arquivosave=ARQUIVOSAVE, exitmode='invoc')
        self.old_mode_invoc = 'expansion_mode'
        self.mode_expansion_state = 'add'
    def estudo(self,NIVEL=None):
        from IPython.display import display
        super(digestor_InvExp,self).estudo(NIVEL)
        #self.mode_invoc_time_countMax = 1*60 # retirar depois
        def subrotina_set_mode_invoc():
            # responsabilidade [ cria o botao ] < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            BUTTON_clock = self.wdg_Clock()
            # responsabilidade [ configura o standby ] < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            self.mode_state = 'invoc' ; self.initStateFlag = False
            # return final < handle_TEXT_AREA < wdg_BrainWasher < creatorWDG
            self.widget.children[0].children[4].value = '<br> <b>Modo Invocação Selecionado : Clique No Botão Abaixo </b><br>'
            display(BUTTON_clock)
        subrotina_set_mode_invoc()        




        