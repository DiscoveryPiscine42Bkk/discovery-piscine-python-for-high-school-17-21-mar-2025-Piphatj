

def checkmate(board):
    rows = board.splitlines()
    king_pos = None
    check=0
    k=0

    for i in range(len(rows)):
        if 'K' in rows[i]:
            king_pos = (i, rows[i].index('K'))
            
            break
    
    if not king_pos:
        print("ksmall")
        return

    bishop_loca=None
    queen_loca=None
    pawn_loca=None
    rook_loca=None
    if king_pos !=None:
        king_row, king_col = king_pos
    for i in range(len(rows)):
        if 'P' in rows[i]:
            pawn_loca=(i, rows[i].index('P'))
            
    for j in range(len(rows)):
        if 'B' in rows[j]:
            bishop_loca=(j, rows[j].index('B'))
            
    for i in range(len(rows)):
        if 'R' in rows[i]:
            rook_loca=(i, rows[i].index('R'))
            
    for i in range(len(rows)):
        if 'Q' in rows[i]:
            queen_loca=(i,rows[i].index('Q'))
    for i in range(len(rows)):
        k += rows[i].count('K') 
    
    
    

    def pawn(pawn_loca):
        p_row , p_col = pawn_loca
        m1=p_row-1 , p_col+1 #ขึ้นบนเลยลบ ไปขวาเลยบวก
        m2=p_row-1 , p_col-1 #
        direc=[m1,m2]
        check_p=0
        for i in direc:
            if i==king_pos:
                
                check_p+=1
            if i == queen_loca or i == rook_loca or i == bishop_loca:
                
                break
        
        return check_p




    def bishop(bishop_loca):
        b_row , b_col = bishop_loca
        d_b1=[]
        d_b2=[]
        d_b3=[]
        d_b4=[]
        check_b=0
        for i in range (len(rows)):#ขวาล่าง
            if b_row<0 or b_col<0 or b_row==len(rows) or b_col==len(rows):
                continue
            else:
                b_row+=1
                b_col+=1
            if b_row<len(rows) and b_col<len(rows) and b_row >=0 and b_col>=0:
                d_b1.append((b_row,b_col))
        
        for i in d_b1:
            if i == king_pos:
                
                check_b+=1
            if i == queen_loca or i == rook_loca or i == pawn_loca:
                
                break



        b_row , b_col = bishop_loca
        for i in range (len(rows)):#ขึ้นมุมซ้ายบน
            if b_row<0 or b_col<0 or b_row==len(rows) or b_col==len(rows):
                continue
            else:
                b_row-=1
                b_col-=1
            if b_row<len(rows) and b_col<len(rows) and b_row >=0 and b_col>=0:
                d_b2.append((b_row,b_col))
        
        for i in d_b2:
            if i == king_pos:
                
                check_b+=1
            if i == queen_loca or i == rook_loca or i == pawn_loca:
                
                break


        b_row , b_col = bishop_loca
        for i in range (len(rows)):#ลงมุมซ้ายล่าง
            if b_row<0 or b_col<0 or b_row==len(rows) or b_col==len(rows):
                continue
            else:
                b_row+=1
                b_col-=1
            if b_row<len(rows) and b_col<len(rows) and b_row >=0 and b_col>=0:
                d_b3.append((b_row,b_col))
        
        for i in d_b3:
            if i == king_pos:
                
                check_b+=1
            if i == queen_loca or i == rook_loca or i == pawn_loca:
                
                break


        b_row , b_col = bishop_loca
        for i in range (len(rows)):#ขึ้นมุมขวาบน
            if b_row<0 or b_col<0 or b_row==len(rows) or b_col==len(rows):
                continue
            else:
                b_row-=1
                b_col+=1
            if b_row<len(rows) and b_col<len(rows) and b_row >=0 and b_col>=0:
                d_b4.append((b_row,b_col))
        
        for i in d_b4:
            if i == king_pos:
                
                check_b+=1
            if i == queen_loca or i == rook_loca or i == pawn_loca:
                
                break
        
        return check_b
        
        
        




    def rook(rook_loca):
        r_row , r_col = rook_loca
        d_r1=[]
        d_r2=[]
        d_r3=[]
        d_r4=[]
        check_r=0

        for i in range (len(rows)):#ขึ้น
            if r_row<0 or r_col<0 or r_row==len(rows) or r_col==len(rows):
                continue
            else:
                r_row-=1
                r_col+=0
            if r_row<len(rows) and r_col<len(rows) and r_row >=0 and r_col>=0:
                d_r1.append((r_row,r_col))
        
        for i in d_r1:
            if i == king_pos:
                
                check_r+=1
            if i == bishop_loca or i == queen_loca or i == pawn_loca:
                
                break


        
        r_row , r_col = rook_loca
        for i in range (len(rows)):#ลง
            if r_row<0 or r_col<0 or r_row==len(rows) or r_col==len(rows):
                continue
            else:
                r_row+=1
                r_col+=0
            if r_row<len(rows) and r_col<len(rows) and r_row >=0 and r_col>=0:
                d_r2.append((r_row,r_col))
        
        for i in d_r2:
            if i == king_pos:
                
                check_r+=1
            if i == bishop_loca or i == queen_loca or i == pawn_loca:
                
                break



        r_row , r_col = rook_loca
        for i in range (len(rows)):#ซ้าย
            if r_row<0 or r_col<0 or r_row==len(rows) or r_col==len(rows):
                continue
            else:
                r_row+=0
                r_col-=1
            if r_row<len(rows) and r_col<len(rows) and r_row >=0 and r_col>=0:
                d_r3.append((r_row,r_col))
        
        for i in d_r3:
            if i == king_pos:
                
                check_r+=1
            if i == bishop_loca or i == queen_loca or i == pawn_loca:
                
                break



        r_row , r_col = rook_loca
        for i in range (len(rows)):#ขวา
            if r_row<0 or r_col<0 or r_row==len(rows) or r_col==len(rows):
                continue
            else:
                r_row+=0
                r_col+=1
            if r_row<len(rows) and r_col<len(rows) and r_row >=0 and r_col>=0:
                d_r4.append((r_row,r_col))
        
        for i in d_r4:
            if i == king_pos:
                
                check_r+=1
            if i == bishop_loca or i == queen_loca or i == pawn_loca:
                
                break
        
        return check_r
        




    def queen(queen_loca):
        (q_row , q_col) = queen_loca
        d_q1=[]
        d_q2=[]
        d_q3=[]
        d_q4=[]
        d_q5=[]
        d_q6=[]
        d_q7=[]
        d_q8=[]
        check_q=0
        for i in range (len(rows)):#ขึ้น
            if q_row<0 or q_col<0 or q_row==len(rows) or q_col==len(rows):
                continue
            else:
                
                q_row-=1
                q_col+=0
                if q_row<len(rows) and q_col<len(rows) and q_row >=0 and q_col>=0:
                    d_q1.append((q_row,q_col))
        
        for i in d_q1:
            if i == king_pos:
                
                check_q+=1
            if i == bishop_loca or i == rook_loca or i == pawn_loca:
                
                break


        q_row , q_col = queen_loca
        for i in range (len(rows)):#ลง
            if q_row<0 or q_col<0 or q_row==len(rows) or q_col==len(rows):
                continue
            else:
                
                q_row+=1
                q_col+=0
                if q_row<len(rows) and q_col<len(rows) and q_row >=0 and q_col>=0:
                    d_q2.append((q_row,q_col))
        
        for i in d_q2:
            if i == king_pos:
                
                check_q+=1
            if i == bishop_loca or i == rook_loca or i == pawn_loca:
                
                break



        (q_row , q_col) = queen_loca
        for i in range (len(rows)):#ซ้าย
            if q_row<0 or q_col<0 or q_row==len(rows) or q_col==len(rows):
                continue
            else:
                
                q_row+=0
                q_col-=1
                if q_row<len(rows) and q_col<len(rows) and q_row >=0 and q_col>=0:
                    d_q3.append((q_row,q_col))
        
        for i in d_q3:
            if i == king_pos:
                
                check_q+=1
            if i == bishop_loca or i == rook_loca or i == pawn_loca:
                
                break




        q_row , q_col = queen_loca
        for i in range (len(rows)):#ขวา
            if q_row<0 or q_col<0 or q_row==len(rows) or q_col==len(rows):
                continue
            else:
                
                q_row+=0
                q_col+=1
                if q_row<len(rows) and q_col<len(rows) and q_row >=0 and q_col>=0:
                    d_q4.append((q_row,q_col))
        
        for i in d_q4:
            if i == king_pos:
                
                check_q+=1
            if i == bishop_loca or i == rook_loca or i == pawn_loca:
                
                break
        q_row , q_col = queen_loca
        for i in range (len(rows)):#ขวาล่าง
            if q_row<0 or q_col<0 or q_row==len(rows) or q_col==len(rows):
                continue
            else:
                
                q_row+=1
                q_col+=1
                if q_row<len(rows) and q_col<len(rows) and q_row >=0 and q_col>=0:
                    d_q5.append((q_row,q_col))
        
        for i in d_q5:
            if i == king_pos:
                
                check_q+=1
            if i == bishop_loca or i == rook_loca or i == pawn_loca:
                
                break

    

        q_row , q_col = queen_loca
        for i in range (len(rows)):#ขึ้นมุมซ้ายบน
            if q_row<0 or q_col<0 or q_row==len(rows) or q_col==len(rows):
                continue
            else:
                
                q_row-=1
                q_col-=1
            if q_row<len(rows) and q_col<len(rows) and q_row >=0 and q_col>=0:
                d_q6.append((q_row,q_col))
        
        for i in d_q6:
            if i == king_pos:
                
                check_q+=1
            if i == bishop_loca or i == rook_loca or i == pawn_loca:
                
                break



        q_row , q_col = queen_loca
        for i in range (len(rows)):#ลงมุมซ้ายล่าง
            if q_row<0 or q_col<0 or q_row==len(rows) or q_col==len(rows):
                continue
            else:
                
                q_row+=1
                q_col-=1
            if q_row<len(rows) and q_col<len(rows) and q_row >=0 and q_col>=0:
                d_q7.append((q_row,q_col))
        
        for i in d_q7:
            if i == king_pos:
                
                check_q+=1
            if i == bishop_loca or i == rook_loca or i == pawn_loca:
                
                break



        q_row , q_col = queen_loca
        for i in range (len(rows)):#ขึ้นมุมขวาบน
            if q_row<0 or q_col<0 or q_row==len(rows) or q_col==len(rows):
                continue
            else:
                
                q_row-=1
                q_col+=1
            if q_row<len(rows) and q_col<len(rows) and q_row >=0 and q_col>=0:
                d_q8.append((q_row,q_col))
        
        for i in d_q8:
            if i == king_pos:
                check_q+=1
            if i == bishop_loca or i == rook_loca or i == pawn_loca:
                
                break
        
        return check_q


    c=0
    c2=0
    for i in range(0,len(rows)):
        
        if len(rows[i])!=len(rows[0]):
            c+=1
    




    if any(len(row) != len(rows) for row in rows):#square check
        c2+=1


    if k==1 and c==0 and c2==0:

        for i in range(len(rows)):
            if 'P' in rows[i]:
                pawn(pawn_loca)
        for j in range(len(rows)):
            if 'B' in rows[j]:
                bishop(bishop_loca)
        for i in range(len(rows)):
            if 'R' in rows[i]:
                rook(rook_loca)
        for i in range(len(rows)):
            if 'Q' in rows[i]:
                queen(queen_loca)



        if pawn_loca!=None:
            n1=pawn(pawn_loca)
        else:
            n1=0

        if bishop_loca!=None:
            n2=bishop(bishop_loca)
        else:
            n2=0

        if rook_loca!=None:
            n3=rook(rook_loca)
        else:
            n3=0

        if queen_loca!=None:
            n4=queen(queen_loca)
        else:
            n4=0
    # if bishop(bishop_loca)>0 or rook(rook_loca)>0 or queen(queen_loca)>0 or pawn(pawn_loca):
    #     print("Success")
        if n1>0 or n2>0 or n3>0 or n4>0:
            print("Success")
        else:
            print("Fail")
             

    elif k>1:
        print("k big")
        return
    elif c!=0:
        print("อย่าแซ่มแล่ม")
        return
    elif c2!=0:
        print("Square!!")
    


