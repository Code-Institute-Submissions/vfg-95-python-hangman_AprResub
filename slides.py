def tornado_display(remaining_guesses):
    slides = [
            """
                              \\\\\\\\\\\\\\\\\\\\             
                              \\\\\\\\\\\\\\\\\              
                              \\\\\\\\\\\\\\\\             
                            \\\\\\\\\\\\\\\              
                    *      \\\\\\\\\\\\\                 
                `         \\\\\\\\\\\\          *      
                      *     \\\\\\\\\\\\      `    `   
                  *        *   \\\\\\\\\\\  *   *     * 
                        `  *   \\\\\\\\\\\   `    * `   
                      *   *   \\\\\\\\\\   *   *        
                      `    *   * \\\\\\\\\  *     * `   
                  *     `   *    \\\\\\___ *    `  *   
                        *  `  * \\\\\`````\  ` *      
                            *  \\\\\\\`````\ *         
                              \\\\\\] | [] |
            """,
            """
                        \\\\\\\\\\\\\\\\\\\\                   
                          \\\\\\\\\\\\\\\\\                  
                          \\\\\\\\\\\\\\\\                 
                        \\\\\\\\\\\\\\\                  
                      \\\\\\\\\\\\\                      
                      \\\\\\\\\\\\                     
                        \\\\\\\\\\\\      `    `       
                      *   \\\\\\\\\\\  *   *             
                    `  *   \\\\\\\\\\\   *  *   `        
                    *   *   \\\\\\\\\\  *                
                  `    *   * \\\\\\\\\ *   *   `         
                    `     *  \\\\\\\ `_____             
                      \ \ \ * \\\\\\ /\`````\          
                    \ \ \ \  \\\\\\ /  \`````\          
                    \ \ \ \ \\\\\\  |[] | [] |

            """,
            """
                     \\\\\\\\\\\\\\\\\\\\                      
                     \\\\\\\\\\\\\\\\\                       
                     \\\\\\\\\\\\\\\\                      
                   \\\\\\\\\\\\\\\                       
                 \\\\\\\\\\\\\                           
                 \\\\\\\\\\\\                          
                   \\\\\\\\\\\\      `    `            
                 *   \\\\\\\\\\\  *   *                  
               `  *   \\\\\\\\\\\   *  *   `             
               *   *   \\\\\\\\\\  *                     
             `    *   * \\\\\\\\\ *   *   `              
               `     *  \\\\\\\\   * `_____             
                 \ \ \ * \\\\\\\  *  /\`````\          
               \ \ \ \  \\\\\\  /   /  \`````\          
               \ \ \ \ \\\\\\ / /   |[] | [] |
            """,
            """
                 \\\\\\\\\\\\\\\\\\\\                          
                 \\\\\\\\\\\\\\\\\                           
                 \\\\\\\\\\\\\\\\                          
               \\\\\\\\\\\\\\\                           
               \\\\\\\\\\\\\                             
               \\\\\\\\\\\\                             
                 \\\\\\\\\\\\      `    `               
               *   \\\\\\\\\\\  *   *                    
           `  *   \\\\\\\\\\\   *  *   `                 
           *   *   \\\\\\\\\\  *                         
         `    *   * \\\\\\\\\ *   *   `                  
             `     *  \\\\\\\\   *   `_____             
             \ \ \ * \\\\\\\  * /   /\`````\          
           \ \ \ \  \\\\\\  / /    /  \`````\          
           \ \ \ \ \\\\\\ / / /    |[] | [] |
            """,
            """
              \\\\\\\\\\\\\\\\\\\\                             
              \\\\\\\\\\\\\\\\\                              
              \\\\\\\\\\\\\\\\                             
             \\\\\\\\\\\\\\\                             
            \\\\\\\\\\\\\                                
            \\\\\\\\\\\\                               
              \\\\\\\\\\\\      `    `                 
            *   \\\\\\\\\\\  *   *                      
        `  *   \\\\\\\\\\\   *  *   `                   
        *   *   \\\\\\\\\\  *                           
      `    *   * \\\\\\\\\ *   *   `                    
          `     *  \\\\\\\\   *      `_____             
          \ \ \ * \\\\\\\  * /      /\`````\          
        \ \ \ \  \\\\\\  / / /     /  \`````\          
        \ \ \ \ \\\\\\ / / /       |[] | [] |
            """,
            """
          \\\\\\\\\\\\\\\\\\\\                                  
        \\\\\\\\\\\\\\\\\                                   
        \\\\\\\\\\\\\\\\                                  
      \\\\\\\\\\\\\\\                                    
      \\\\\\\\\\\\\                                      
      \\\\\\\\\\\\                                     
        \\\\\\\\\\\\      `    `                       
      *   \\\\\\\\\\\  *   *                            
  `    *   \\\\\\\\\\\\   *  *   `                      
    *   *   \\\\\\\\\\  *                               
  `    *   * \\\\\\\\\ *   *   `                        
    `     *  \\\\\\\\   *            `_____            
    \ \ \ * \\\\\\\  * /            /\`````\          
  \ \ \ \  \\\\\\  / / /           /  \`````\          
  \ \ \ \ \\\\\\ / / / /           |[] | [] |
            """
    ]
    return slides[remaining_guesses]
