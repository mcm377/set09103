 f r o m   f l a s k   i m p o r t   F l a s k ,   r e n d e r _ t e m p l a t e 
 #   c o d i n g :   u t f - 8 
 
 a p p   =   F l a s k ( _ _ n a m e _ _ ) 
 
 @ a p p . r o u t e ( " / " ) 
 d e f   r o o t ( ) : 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' i n d e x . h t m l ' ) 
 
 @ a p p . r o u t e ( " / a r t i s t s / " ) 
 d e f   a r t i s t s ( ) : 
         a r t i s t s   =   [ ' A v i c i i ' ,   ' B u g z y   M a l o n e ' ,   ' C a l v i n   H a r r i s ' ,   ' C l e a n   B a n d i t ' ,   ' D r a k e ' ,   ' E r i   K i t a m u r a ' ,   ' G o r g o n   C i t y ' ,   ' K a n o ' ,   ' T h e   K i l l e r s ' ,   ' N e r o ' ,   ' R u d i m e n t a l ' ,   ' T R F ' ] 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' a r t i s t s . h t m l ' ,   a r t i s t s   =   a r t i s t s ) 
 
 @ a p p . r o u t e ( " / a r t i s t s / < a r t i s t > " ) 
 d e f   g e t _ a r t i s t ( a r t i s t ) : 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' a r t i s t _ d e t a i l s . h t m l ' ,   a r t i s t   =   a r t i s t ) 
 
 @ a p p . r o u t e ( " / a l b u m s / " ) 
 d e f   a l b u m s ( ) : 
         a l b u m s   =   s o r t e d ( [ ' T r u e ' ,   ' W a l k   W i t h   M e ' ,   ' I   C r e a t e d   D i s c o ' ,   ' R e a d y   F o r   T h e   W e e k e n d ' ,   ' 1 8   M o n t h s ' ,   ' M o t i o n ' ,   ' N e w   E y e s ' ,   ' 2 0 1 0 ' ,   ' O r i g i n L   C l a s s C ' ,   ' L i v e   f r o n   F r a n c e ' ,   ' T h a n k   M e   L a t e r ' ,   ' T a k e   C a r e ' ,   ' N o t h i n g   W a s   T h e   S a m e ' ,   ' R e ; S t o r y ' ,   u ' S h o m e i   (�< �f ) ' ,   ' S i r e n s ' ,   ' T h e   C r y p t ' ,   ' R e a l ' ,   ' H o m e   S w e e t   H o m e ' ,   ' L o n d o n   T o w n ' ,   ' 1 4 0   G r i m e   S t r e e t ' ,   ' M e t h o d   T o   T h e   M e a d n e s s ' ,   ' W e l c o m e   R e a l i t y ' ,   ' B e t w e e n   I I   W o r l d s ' ,   ' H o m e ' ,   ' W e   T h e   G e n e r a t i o n ' ,   ' H o t   F u s s ' ,   ' S a m s   T o w n ' ,   ' D a y   &   A g e ' ,   ' B a t t l e   B o r n ' ,   ' G R A V I T Y ' ] ) 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' a l b u m s . h t m l ' ,   a l b u m s   =   a l b u m s ) 
 
 @ a p p . r o u t e ( " / a l b u m s / < a l b u m > " ) 
 d e f   g e t _ a l b u m ( a l b u m ) : 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' a l b u m _ d e t a i l s . h t m l ' ,   a l b u m   =   a l b u m ) 
 
 @ a p p . r o u t e ( " / g e n r e s / " ) 
 d e f   g e n r e s ( ) : 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' g e n r e s . h t m l ' ) 
 
 @ a p p . r o u t e ( " / t r a c k s / " ) 
 d e f   t r a c k s ( ) : 
         r e t u r n   r e n d e r _ t e m p l a t e ( ' t r a c k s . h t m l ' ) 
 
 i f   _ _ n a m e _ _   = =   " _ _ m a i n _ _ " :   
         a p p . r u n ( h o s t = ' 0 . 0 . 0 . 0 ' ,   d e b u g = T r u e ) 
