

| HOOK                   | OBJET                               |
|------------------------|-------------------------------------|
| ngOnChanges            | Se lance lorsqu'Angular modifie une des propriétés du Component / directive suite à un Property Binding @Input. La méthode reçoit un object SimpleChanges contenant les valeurs courantes et précédentes |
| ngOnInit               | Initialise le component / directive après qu'Angular ait valorisé les Property Binding @Input |
| ngDoCheck              | Détecte et agit sur les changements qu'Angular ne peut ou ne pourra pas détecter lui même. Il permet, en outre, de vérifier les changements dans les directives additionnelement aux algorithmes classiques |
| ngAfterContentInit     | Il se lance également après l'initialisation d'un Content ( ng-content ). A partir de ce moment, les propriétés initialisées par @ContentChild et @ContentChildren sont valorisées |
| ngAfterContentChecked  | |
| ngAfterViewInit        | Se lance après qu'Angular initialise la vue (template) du Component et les vues enfants.  A partir de ce moment, les propriétés initialisées par @ViewChild et @ViewChildren sont valorisées |
| ngAfterViewInitChecked | |
| ngOnDestroy            | Se lance juste avant qu'Angular ne détruise le Component / directive. C'est l'endroit idéal pour desinscrire les Observables et détacher les évènements afin d'éviter les fuites mémoires |



         (input property sets/resets)
                      |
                      |
        +----------------------------+
        | ngOnChanges(SimpleChanges) |
        +----------------------------+
              |                |
            (1st)         (subsequent)
              |                |
        +----------+     +-----------+
        | ngOnInit |-->--| ngDoCheck |---->------>---->----+
        +----------+     +-----------+                     |
                              |                            |
                            (1st)                     (subsequent)
                              |                            |
                     +--------------------+     +-----------------------+
                     | ngAfterContentInit |-->--| ngAfterContentChecked |---->---->----+
                     +--------------------+     +-----------------------+              |
                                                           |                           |
                                                         (1st)                    (subsequent)
                                                           |                           |
                                                  +-----------------+         +--------------------+
                                                  | ngAfterViewInit |---->----| ngAfterViewChecked |
                                                  +-----------------+         +--------------------+
    
    
    
        +-------------+
        | ngOnDestroy |---->----[[[Angular destroys directive or component]]]
        +-------------+
