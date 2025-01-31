self.gs = np.array([
    np.array(['bR', 'bN', 'bB', '--', 'bK', 'bB', 'bN', 'bR']),  # Row 0: Black major pieces
    np.array(['bP', 'bP', '--', '--', 'bP', 'bP', 'bP', 'bP']),  # Row 1: Black pawns
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 2: Empty
    np.array(['--', 'wN', 'bP', 'bP', '--', '--', '--', '--']),  # Row 3: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 4: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 5: Empty
    np.array(['bQ', 'wP', 'wP', 'wP', 'wQ', 'wP', 'wP', 'wP']),  # Row 6: White pawns
    np.array(['wR', 'wN', 'wB', '--', 'wK', 'wB', '--', 'wR'])   # Row 7: White major pieces
])

self.gs = np.array([
    np.array(['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']),  # Row 0: Black major pieces
    np.array(['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP']),  # Row 1: Black pawns
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 2: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 3: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 4: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 5: Empty
    np.array(['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']),  # Row 6: White pawns
    np.array(['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'])   # Row 7: White major pieces
])

self.gs = np.array([
    np.array(['bR', 'bN', 'bB', '--', 'bK', 'bB', '--', 'bR']),  # Row 0: Black major pieces
    np.array(['bP', 'bP', 'bP', 'bP', '--', 'bP', '--', 'bP']),  # Row 1: Black pawns
    np.array(['--', '--', '--', '--', '--', 'wK', '--', '--']),  # Row 2: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 3: Empty
    np.array(['--', '--', 'wQ', '--', '--', '--', '--', '--']),  # Row 4: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 5: Empty
    np.array(['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']),  # Row 6: White pawns
    np.array(['wR', 'wN', 'wB', '--', '--', 'wB', 'wN', 'wR'])   # Row 7: White major pieces
])


 
import numpy as np
import random
class Gamestate:
    def __init__(self):
        self.gs = np.array([
    np.array(['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']),  # Row 0: Black major pieces
    np.array(['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP']),  # Row 1: Black pawns
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 2: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 3: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 4: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 5: Empty
    np.array(['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']),  # Row 6: White pawns
    np.array(['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'])   # Row 7: White major pieces
])
        self.rook_moved = {'wR_0': False, 'wR_7': False, 'bR_0': False, 'bR_7': False}
        self.king_moved = {'wK': False, 'bK': False}
        self.rookClicked = False
        self.kingClicked = False
        self.loc = None
        self.in_check = False
        self.kingspos = {'wK':(7,4), 'bK':(0,4)}

    def attackline(self, piece, white_turn):
        xn,yn = piece[0],piece[1]
        
            
        line=[]
        if white_turn:
            x,y = self.kingspos['wK']
        else:
            x,y = self.kingspos['bK']
        if self.gs[xn,yn][1]=='N':
            return [(xn,yn)]
        
        dx,dy = x-piece[0], y-piece[1]
        i=1
        while (xn,yn) != (x,y):
            line.append((xn,yn))
            if dx==0:
                yn = piece[1]+dy/abs(dy)*i
                i+=1
            elif dy==0:
                xn = piece[0]+dx/abs(dx)*i
                i+=1
            else:
                xn = piece[0]+dx/abs(dx)*i
                yn = piece[1]+dy/abs(dy)*i
                i+=1    
        return line       


    def is_in_check(self, gs, white_turn) : 
        if white_turn:
            coords = self.kingspos['wK']
            kn_p = self.knight_moves(coords, white_turn)
            
            for x,y in kn_p:
                if gs[x,y]=='bN':
                    return True, (x,y), coords
            b_p = self.bishop_moves(coords, white_turn)
            for x,y in b_p:
                if gs[x,y]=='bB':
                    return True, (x,y), coords

            r_p = self.rook_moves(coords, white_turn)
            for x,y in r_p:
                if gs[x,y]=='bR':
                     return True, (x,y),coords

            q_p = self.queen_moves(coords, white_turn)
            for x,y in q_p:
                if gs[x,y]=='bQ':
                     return True, (x,y),coords

        else:
            coords = self.kingspos['bK']
            kn_p = self.knight_moves(coords, white_turn)
            for x,y in kn_p:
                if gs[x,y]=='wN':
                    return True, (x,y),coords
            b_p = self.bishop_moves(coords, white_turn)
            for x,y in b_p:
                if gs[x,y]=='wB':
                    return True, (x,y),coords
            r_p = self.rook_moves(coords, white_turn)
            for x,y in r_p:
                if gs[x,y]=='wR':
                    return True, (x,y),coords
            q_p = self.queen_moves(coords, white_turn)
            for x,y in q_p:
                if gs[x,y]=='wQ':
                    return True, (x,y),coords
        return False, None,coords





    def legal_moves(self, coords, white_turn):
        piece = self.gs[coords[0], coords[1]]
        
        if piece == 'wR' or piece == 'bR':
            self.rookClicked = True
            return self.rook_moves(coords, white_turn)
        elif piece == 'wN' or piece == 'bN':
            return self.knight_moves(coords, white_turn)
        elif piece == 'wB' or piece == 'bB':
            return self.bishop_moves(coords, white_turn)
        elif piece == 'wQ' or piece == 'bQ':
            return self.queen_moves(coords, white_turn)
        elif piece == 'wK' or piece == 'bK':
            self.kingClicked = True
            return self.king_moves(coords, white_turn)
        elif piece == 'wP' or  piece == 'bP':
            return self.pawn_moves(coords, white_turn)
        else:
            return []

    def rook_moves(self, coords, white_turn):
        moves = []
        x,y = coords[0], coords[1]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]       
        for dx, dy in directions:
            for i in range(7):
                xn, yn = (x+dx*(i+1)), (y+dy*(i+1))   
                if 0 <= xn <= 7 and 0 <= yn <= 7:
                    if self.gs[xn, yn] != '--':
                        if  (self.piece_type((xn,yn)) ^ white_turn):
                            moves.append((xn, yn))
                            break
                        else:
                            break
                    else:
                        moves.append((xn,yn))
        
        return moves

    def knight_moves(self, coords, white_turn):
        x, y = coords
        move_vectors = np.array([(1, 2), (-1, 2), (-1, -2), (1, -2), (2, 1), (-2, 1), (-2, -1), (2, -1)])
        pre_filtered_moves = move_vectors + np.array([x, y])
        
        # Ensure moves are within board bounds
        valid_moves = (pre_filtered_moves[:, 0] >= 0) & (pre_filtered_moves[:, 0] <= 7) & (pre_filtered_moves[:, 1] >= 0) & (pre_filtered_moves[:, 1] <= 7)
        pre_filtered_moves = pre_filtered_moves[valid_moves]
        
        # Filter by white or black pieces
        moves = []
        for move in pre_filtered_moves:
            xn, yn = move
            if self.gs[xn, yn] != '--':  # If not empty
                if (self.piece_type((xn, yn)) ^ white_turn):
                    moves.append((xn, yn))
            else:
                moves.append((xn, yn))
        # if king in check just move to nullify check
        if self.in_check:
                    enemy_attack = self.attackline(self.loc, white_turn)
                    moves = list(set(moves) & set(enemy_attack))
        # pin logic
        if d_coords in moves:
                    
                    temp_board = self.gs
                    self.temp_board[d_coords[0], d_coords[1]] = self.temp_board[coords[0], coords[1]]
                    self.temp_board[coords[0], coords[1]] = '--'

                    # pin logic i know that it dont look good but what ever
                    self.in_check, self.loc, kingloc = self.is_in_check(temp_board,white_turn)
                    if self.in_check:
                        moves.remove(d_coords)
        return moves


        

    def bishop_moves(self, coords, white_turn):
        x,y = coords[0], coords[1]
        moves=[]
        x1 = 7-coords[0]
        y1 = 7 - coords[1]
        for i in range(1, min(x,y)+1):
            
            if self.gs[x-i, y-i] != '--':
                    if  (self.piece_type((x-i,y-i)) ^ white_turn):
                        moves.append((x-i, y-i))
                        break
                    else:
                        break
            else:
                moves.append((x-i, y-i))
        for i in range(1,min(x1,y)+1):
               
            if self.gs[x+i,y-i] != '--':
                    if  (self.piece_type((x+i,y-i)) ^ white_turn):
                        moves.append((x+i, y-i))
                        break
                    else:
                        break
            else:
                moves.append((x+i, y-i))
        for i in range(1,min(x,y1)+1):
            
            if self.gs[x-i,y+i] != '--':
                    if  (self.piece_type((x-i,y+i)) ^ white_turn):
                        moves.append((x-i, y+i))
                        break
                    else:
                        break
            else:
                moves.append((x-i, y+i))
        for i in range(1,min(x1,y1)+1):
            
            if self.gs[x+i,y+i] != '--':
                    if  (self.piece_type((x+i,y+i)) ^ white_turn):
                        moves.append((x+i, y+i))
                        break
                    else:
                        break
            else:
                moves.append((x+i, y+i))
        return moves

    def queen_moves(self, coords,white_turn):
        moves = []
        moves.extend(self.bishop_moves(coords,white_turn))
        moves.extend(self.rook_moves(coords, white_turn))
        return moves

    def king_moves(self, coords, white_turn):
        x,y = coords[0], coords[1]
        castling_move = None
        moves = []
        directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for dx, dy in directions:
            xn,yn = x+dx, y+dy
            if 0 <= xn <= 7 and 0 <= yn <= 7:
                if not self.box_attack((xn,yn),white_turn):
                    if self.gs[xn,yn] != '--':
                        if  (self.piece_type((xn,yn)) ^ white_turn):                                                
                                moves.append((xn,yn))
                    else:                     
                        moves.append((xn,yn))
        return moves


    def check_castling(self, coords, white_turn):
        x,y = coords[0],coords[1]
        castling_move = []
        if white_turn:
            if not (self.king_moved['wK']):
                ks, qs = self.check_sides(coords) 
                if ks:
                    if not (self.rook_moved['wR_7']):
                        safe = True
                        for i in range(2):
                            xc,yc = x,y+i+1
                            if self.box_attack((xc,yc),white_turn):
                                safe = False
                                break
                        if safe:
                            castling_move.append((7, 6))
                if qs:
                    if not self.rook_moved['wR_0']:
                        safe = True
                        for i in range(3):
                            xc,yc = x,y+i+1
                            if self.box_attack((xc,yc),white_turn):
                                safe = False
                                break
                        if safe:
                            castling_move.append((7, 2))
        else:
            if not (self.king_moved['bK']):
                ks, qs = self.check_sides(coords)
                if ks:
                    if not self.rook_moved['bR_7']:     
                        safe = True
                        for i in range(2):
                            xc,yc = x,y+i+1
                            if self.box_attack((xc,yc),white_turn):
                                safe = False
                                break
                        if safe:
                            castling_move.append((0, 6))
                if qs:
                    if not self.rook_moved['bR_0']:
                        safe = True
                        for i in range(3):
                            xc,yc = x,y+i+1
                            if self.box_attack((xc,yc),white_turn):
                                safe = False
                                break
                        if safe:
                            castling_move.append((0, 2))

        return castling_move

    def check_sides(self, coords):
        x,y = coords[0],coords[1]
        queenside_available = True 
        kingside_available = True
        for i in range(2):
            if self.gs[x,y+i+1]!='--':
                kingside_available = False
                break
        for i in range(3):
            if self.gs[x,y-i-1]!='--':
                queenside_available = False
                break
        return kingside_available,queenside_available

    def box_attack(self, coords, white_turn):       
        if white_turn:
            kn_p = self.knight_moves(coords, white_turn)
            for x,y in kn_p:
                if self.gs[x,y]=='bN':
                    return True
            b_p = self.bishop_moves(coords, white_turn)
            for x,y in b_p:
                if self.gs[x,y]=='bB':
                    return True
            r_p = self.rook_moves(coords, white_turn)
            for x,y in r_p:
                if self.gs[x,y]=='bR':
                    return True
            q_p = self.queen_moves(coords, white_turn)
            for x,y in q_p:
                if self.gs[x,y]=='bQ':
                    return True
        else:
            kn_p = self.knight_moves(coords, white_turn)
            for x,y in kn_p:
                if self.gs[x,y]=='wN':
                    return True
            b_p = self.bishop_moves(coords, white_turn)
            for x,y in b_p:
                if self.gs[x,y]=='wB':
                    return True
            r_p = self.rook_moves(coords, white_turn)
            for x,y in r_p:
                if self.gs[x,y]=='wR':
                    return True
            q_p = self.queen_moves(coords, white_turn)
            for x,y in q_p:
                if self.gs[x,y]=='wQ':
                    return True
        return False



    def pawn_moves(self, coords, white_turn):
        x,y = coords[0], coords[1]
        moves = []
        capture_pos_b = [(1,-1),(1,1)]
        capture_pos_w = [(-1,-1),(-1,1)]
        if white_turn:
            for dx, dy in capture_pos_w:
                xn,yn = dx+x, dy+y
                if 0 <= xn <= 7 and 0 <= yn <= 7:
                    if self.gs[x+dx, y+dy][0]=='b':
                        moves.append((xn, yn))

            if x == 6:
                new_pos = [(x-2,y),(x-1, y)]
                for pos in new_pos:
                    if self.gs[pos[0],pos[1]] == '--':
                        moves.append(pos)
            else:
                if self.gs[x-1, y] == '--':
                    moves.append((x-1,y))
            
        else:
            for dx, dy in capture_pos_b:
                xn,yn = dx+x, dy+y
                if 0 <= xn <= 7 and 0 <= yn <= 7:
                    if self.gs[xn, yn][0]=='w':
                        moves.append((xn, yn))
            if x == 1:
                new_pos = [(x+2, y),(x+1, y)]
                for pos in new_pos:
                    if self.gs[pos[0],pos[1]] == '--':
                        moves.append(pos)


            else:
                if self.gs[x+1, y] == '--':
                    moves.append((x+1, y))
        return moves

    def make_move(self, coords, d_coords, white_turn):
        is_white = self.piece_type(coords)
        piece = self.gs[coords[0],coords[1]]
        if not (is_white ^ white_turn): 
            if self.valid_castling_move(coords, d_coords):
                moves = self.check_castling(coords, white_turn)
                if d_coords in moves:
                    # Update king and rook positions for castling
                    self.king_moved[self.gs[coords[0], coords[1]]] = True
                    self.gs[d_coords[0], d_coords[1]] = self.gs[coords[0], coords[1]]
                    self.gs[coords[0], coords[1]] = '--'
                    self.kingspos[self.gs[coords[0], coords[1]]] = (d_coords[0], d_coords[1])
                    # Update rook position for castling
                    if d_coords[1] == 2:  # Queen-side
                        self.rook_moved[self.gs[coords[0], 0] + '_0'] = True
                        self.gs[coords[0], 3] = self.gs[coords[0], 0]
                        self.gs[coords[0], 0] = '--'
                    elif d_coords[1] == 6:  # King-side
                        self.rook_moved[self.gs[coords[0], 7] + '_7'] = True
                        self.gs[coords[0], 5] = self.gs[coords[0], 7]
                        self.gs[coords[0], 7] = '--'
                    return not white_turn

            else:
                moves = self.legal_moves(coords, white_turn)
                
                if d_coords in moves:
                    # Update moved status if rook or king is moved
                    if self.rookClicked:
                        self.rook_moved[self.gs[coords[0], coords[1]] + f"_{coords[1]}"] = True
                        
                    elif self.kingClicked:
                        self.king_moved[self.gs[coords[0], coords[1]]] = True
                        self.kingspos[self.gs[coords[0], coords[1]]] = d_coords
                    
                    # Move piece
                    temp_piece_location = self.gs[d_coords[0], d_coords[1]]
                    self.gs[d_coords[0], d_coords[1]] = self.gs[coords[0], coords[1]]
                    self.gs[coords[0], coords[1]] = '--'

                    # pin logic i know that it dont look good but what ever
                    self.in_check, self.loc, kingloc = self.is_in_check(white_turn)
                    if self.in_check:
                        self.gs[coords[0], coords[1]] = self.gs[d_coords[0], d_coords[1]] # go back to the original board dont make change
                        self.gs[d_coords[0], d_coords[1]] = temp_piece_location
                        return white_turn

                    white_turn =  not white_turn
        self.rookClicked = False    
        self.kingClicked = False
        print(self.kingClicked)
        return white_turn


    def piece_type(self, coords):
        piece = self.gs[coords[0],coords[1]]
        return piece[0]=='w'


    def valid_castling_move(self, coords, d_coords):
        valid=False
        if self.gs[coords[0],coords[1]][1]=='K':
            if d_coords[0]==coords[0]==0 or d_coords[0]==coords[0]==7:
                if abs(d_coords[1]-coords[1])==2:
                    valid = True
        return valid
            
    def generateRandom(self, white_turn=False):
        blackpos=[]
        for r in range(8):
            for c in range(8):
                if self.gs[r,c][0]=='b':
                    blackpos.append((r,c))
        moves=[]
        
        while moves==[]:
            origin = random.choice(blackpos)
            moves = self.legal_moves(origin, white_turn)
            
        dest = random.choice(moves)
        return origin, dest

    def check_checkmate(self,white_turn):
        self.in_check, self.loc, kingloc = self.is_in_check(self.gs,white_turn)
        print(self.in_check, self.loc, white_turn)
        if self.in_check:
            if self.king_moves(kingloc, white_turn)!=[]: #if king has some moves then its not checkmate
                return False

            pos = []
            mate = True
            turn = 'b'
            if white_turn:
                turn = 'w'
            for r in range(8):
                for c in range(8):         
                    if self.gs[r,c][0]==turn:
                        pos.append((r,c))
            enemy_attack = self.attackline(self.loc, white_turn)
            for p in pos:
                if p == (1,7):
                    pass
                moves = self.legal_moves(p, white_turn)
                self.kingClicked=False #i know its cheezy but it works
                moves = list(set(moves) & set(enemy_attack))
                if moves != []:
                    mate = False
                    break
            return mate
        else:
            return False





if __name__== '__main__':
    pass
    



if self.in_check:
                    enemy_attack = self.attackline(self.loc, white_turn)
                    print('enemy_attack ', enemy_attack)
               
                        dir = enemy_attack[-1]
                        if piece[1]!='N':          # because knights do have laser attacks so dont need to consider forbidden positions
                            forbiddenpos = (int((2*coords[0]-dir[0])), int((2*coords[1]-dir[1])))
                            if forbiddenpos in moves:
                                moves.remove(forbiddenpos)
                        
                        print(moves)                