# checkmate.py

def checkmate(board):
    # Convert the board string into a list of rows
    rows = board.splitlines()
    
    # Find the position of the King ('K')
    king_pos = None
    for i in range(len(rows)):
        if 'K' in rows[i]:
            king_pos = (i, rows[i].index('K'))
            print(f"King : {king_pos}")
            break
    
    if not king_pos:
        return  # No King found, nothing to check
    
    king_row, king_col = king_pos

    rook_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Directions for Bishop/Queen (diagonal)
    bishop_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # Directions for Pawn (two directions)
    pawn_directions = [(-1, -1), (-1, 1)] if king_row > 0 else []
    

    def pawn(pawn_loca):
        p_row , p_col = pawn_loca
        m1=p_row-1 , p_col+1 #ขึ้นบนเลยลบ ไปขวาเลยบวก
        m2=p_row-1 , p_col-1 #
        direc=[m1,m2]
        for i in direc:
            if i==king_pos:
                print("success")

    def bishop(bishop_loca):
        p_row , p_col = pawn_loca
        m1=p_row-1 , p_col+1 #ขึ้นบนเลยลบ ไปขวาเลยบวก
        m2=p_row-1 , p_col-1 #
        direc=[m1,m2]
        for i in direc:
            if i==king_pos:
                print("success")

    def rook(rook_loca):
        p_row , p_col = pawn_loca #มาคตำแหน่งของหมาก
        #วิธีเดินของหมาก
        m1=p_row-1 , p_col+1 #ขึ้นบนเลยลบ ไปขวาเลยบวก
        m2=p_row-1 , p_col-1 #
        direc=[m1,m2] 
        for i in direc:
            if i==king_pos:
                print("success")

    def queen(queen_loca):
        p_row , p_col = pawn_loca
        m1=p_row-1 , p_col+1 #ขึ้นบนเลยลบ ไปขวาเลยบวก
        m2=p_row-1 , p_col-1 #
        direc=[m1,m2]
        for i in direc:
            if i==king_pos:
                print("success")





    for i in range(len(rows)):
        if 'P' in rows[i]:
            pawn_loca=(i, rows[i].index('P'))
            print(f"Pawn : {pawn_loca}")
            pawn(pawn_loca)
    for j in range(len(rows)):
        if 'B' in rows[j]:
            bishop_loca=(j, rows[j].index('B'))
            print(f"Bishop : {bishop_loca}")
    for i in range(len(rows)):
        if 'R' in rows[i]:
            rook_loca=(i, rows[i].index('R'))
            print(f"Rook : {rook_loca}")
    for i in range(len(rows)):
        if 'Q' in rows[i]:
            queen_loca=(i,rows[i].index('Q'))
            print(f"Queen : {queen_loca}")
    
    



    #



    # # Check for Pawn attack
    # for dr, dc in pawn_directions:
    #     r, c = king_row + dr, king_col + dc
    #     if 0 <= r < len(rows) and 0 <= c < len(rows[0]):
    #         if rows[r][c] == 'P':
    #             print("Success")
    #             return
    
    # # Check for Bishop and Queen attacks (diagonals)
    # for dr, dc in bishop_directions:
    #     r, c = king_row + dr, king_col + dc
    #     while 0 <= r < len(rows) and 0 <= c < len(rows[0]):
    #         if rows[r][c] == 'B' or rows[r][c] == 'Q':
    #             print("Success")
    #             return
    #         elif rows[r][c] != '.':
    #             break
    #         r += dr
    #         c += dc

    # # Check for Rook and Queen attacks (horizontal and vertical)
    # for dr, dc in rook_directions:
    #     r, c = king_row + dr, king_col + dc
    #     while 0 <= r < len(rows) and 0 <= c < len(rows[0]):
    #         if rows[r][c] == 'R' or rows[r][c] == 'Q':
    #             print("Success")
    #             return
    #         elif rows[r][c] != '.':
    #             break
    #         r += dr
    #         c += dc
    
    # # If no piece can attack the King, print "Fail"
    # print("Fail")



# # checkmate.py

# def checkmate(board):
#     # Convert the board string into a list of rows
#     rows = board.splitlines()
    
#     # Find the position of the King ('K')
#     king_pos = None
#     for i in range(len(rows)):
#         if 'K' in rows[i]:
#             king_pos = (i, rows[i].index('K'))
#             break
    
#     if not king_pos:
#         return  # No King found, nothing to check
    
#     king_row, king_col = king_pos
    

#     rook_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     # Directions for Bishop/Queen (diagonal)
#     bishop_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
#     # Directions for Pawn (two directions)
#     pawn_directions = [(-1, -1), (-1, 1)] if king_row > 0 else []

#     # Check for Pawn attack
#     for dr, dc in pawn_directions:
#         r, c = king_row + dr, king_col + dc
#         if 0 <= r < len(rows) and 0 <= c < len(rows[0]):
#             if rows[r][c] == 'P':
#                 print("Success")
#                 return
    
#     # Check for Bishop and Queen attacks (diagonals)
#     for dr, dc in bishop_directions:
#         r, c = king_row + dr, king_col + dc
#         while 0 <= r < len(rows) and 0 <= c < len(rows[0]):
#             if rows[r][c] == 'B' or rows[r][c] == 'Q':
#                 print("Success")
#                 return
#             elif rows[r][c] != '.':
#                 break
#             r += dr
#             c += dc

#     # Check for Rook and Queen attacks (horizontal and vertical)
#     for dr, dc in rook_directions:
#         r, c = king_row + dr, king_col + dc
#         while 0 <= r < len(rows) and 0 <= c < len(rows[0]):
#             if rows[r][c] == 'R' or rows[r][c] == 'Q':
#                 print("Success")
#                 return
#             elif rows[r][c] != '.':
#                 break
#             r += dr
#             c += dc
    
#     # If no piece can attack the King, print "Fail"
#     print("Fail")
